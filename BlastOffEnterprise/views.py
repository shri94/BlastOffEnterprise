from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from BlastOffEnterprise import models
from django.core import serializers
from .filter import EmployeeFilter
import json

@login_required
def dashboard(request):
    user = request.user
    auth0user = user.social_auth.filter(provider="auth0")[0]
    userdata = {
        'user_id' : auth0user.uid,
        'name': user.first_name,
       # 'picture': auth0user.extra_data['picture']
    }
    
    employeeq = models.Employees.objects.all()[:500]
    paginator = Paginator(employeeq, 25)

    page = request.GET.get('page')
    employees = paginator.get_page(page)
    employee_serialize =  serializers.serialize("json", employeeq)

    return render(request, 'dashboard.html', {
        'auth0User': auth0user,
        'userdata': json.dumps(userdata, indent=4),
        'employees': employees
    })

def home(request):
    return render(request, 'home.html')

def navbar(request):
    return render(request, 'navbar.html')

def search(request):
    emp_list = models.Employees.objects.all()
    emp_filter = EmployeeFilter(request.GET, queryset=emp_list)

    return render(request, 'search.html', {'filter': emp_filter})

def empprofile(request, emp_no = None):
    if models.Employees.objects.get(emp_no=emp_no):
        employee = models.Employees.objects.get(emp_no=emp_no)
        salary = models.Salaries.objects.filter(emp_no=emp_no)
        department = models.Departments.objects.get(deptemp=emp_no)
        salary_serialize = serializers.serialize("json", salary)
        title = models.Titles.objects.filter(emp_no=emp_no)
        title_serialize = serializers.serialize("json", title)
        manager = models.Departments.objects.filter(deptemp = emp_no).values('deptmanager')
        managers = []
        for man in manager:
            managers.append(models.Employees.objects.get(emp_no=man['deptmanager']))

        return render(request, 'employee.html', {
            'employee': employee,
            'salary': json.loads(salary_serialize),
            'department': department,
            'title' : json.loads(title_serialize),
            'managers': managers
            })
    else:
        return render('Employee Missing!')

def depprofile(request, dept_no = None):
    if models.Departments.objects.get(dept_no=dept_no):
        department = models.Departments.objects.filter(dept_no=dept_no).values('dept_name', 'deptemp', 'deptmanager')[:300]
        employees = []
        managers = []
        for d in range(0,len(department)):
            employees.append(models.Employees.objects.get(emp_no= department[d]['deptemp']))
            managers.append(models.Employees.objects.get(emp_no= department[d]['deptmanager']))
        return render(request, 'department.html', {
            'department': department,
            'employees': employees


            })
    else:
        return render('No Department found!')


