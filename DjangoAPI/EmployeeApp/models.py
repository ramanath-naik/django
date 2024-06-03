from django.db import models

# Create your models here.

class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=200)

    # class Meta:
    #     db_table = 'custom_table_name' # specifying manual table name

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=200)
    Department = models.CharField(max_length=200)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=500)