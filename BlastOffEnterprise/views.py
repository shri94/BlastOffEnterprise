from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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
    
    employeeq = models.Employees.objects.all()[:10]
    employee_serialize =  serializers.serialize("json", employeeq)

    return render(request, 'dashboard.html', {
        'auth0User': auth0user,
        'userdata': json.dumps(userdata, indent=4),
        'employeeq': json.loads(employee_serialize)
    })

def home(request):
    return render(request, 'home.html')

def navbar(request):
    return render(request, 'navbar.html')

def search(request):
    emp_list = models.Employees.objects.all()[:100]
    emp_filter = EmployeeFilter(request.GET, queryset=emp_list)

    return render(request, 'search.html', {'filter': emp_filter})

