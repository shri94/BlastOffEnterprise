from django.test import TestCase
from BlastOffEnterprise import models

class EmployeeTestCase(TestCase):
    def setUp(self):
        Ftest = models.Employees.objects.create(first_name="test", last_name ="case" ,gender="F")
        Mtest = models.Employees.objects.create(first_name="test2", last_name = "case2",gender="M")
    def test_for_employees(self):
        test = models.Employees.objects.get(name="Ftest")
        test2 = models.Employees.objects.get(name="Mtest")
        self.assertEqual(test.gender,"F")
        self.assertEqual(test.gender,"M")
