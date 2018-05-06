from django.contrib.auth.models import User
import django_filters

class EmployeeFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', ]