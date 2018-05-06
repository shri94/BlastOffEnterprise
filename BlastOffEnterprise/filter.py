#from django.contrib.auth.models import User
from .models import Employees
import django_filters

class EmployeeFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Employees
        fields = [ 'first_name', 'last_name', ]