from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Role(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100, null=True)
    dob = models.DateField(null=True)
    doj = models.DateField(null=True)
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, blank=True, null=True)
    role = models.ForeignKey(
        Role, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    zipcode = models.CharField(max_length=6, null=True)
    leaves = models.IntegerField(null=True, default=0)
    active = models.BooleanField(default=True)
    on_leave = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
