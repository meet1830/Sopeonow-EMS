from django.db import models

# Create your models here.


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=200)
    objects = models.Manager()

    def __str__(self) -> str:
        return self.role_name


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=200)
    objects = models.Manager()

    def __str__(self) -> str:
        return self.department_name


class Employee(models.Model):
    name = models.CharField(max_length=100, null=True)
    dob = models.DateField(null=True)
    doj = models.DateField(null=True)
    department_id = models.ForeignKey(
        Department, on_delete=models.DO_NOTHING, max_length=50, null=True)
    role_id = models.ForeignKey(
        Role, on_delete=models.DO_NOTHING, max_length=50, null=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    zipcode = models.CharField(max_length=50, null=True)
    leave_count = models.IntegerField(null=True, default=0)
    active = models.BooleanField(default=True)
    on_leave = models.BooleanField(default=False)
    objects = models.Manager()

    def __str__(self) -> str:
        return self.name
