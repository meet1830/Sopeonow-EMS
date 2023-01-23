from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100, null=True)
    dob = models.DateField(null=True)
    doj = models.DateField(null=True)
    department = models.CharField(max_length=50, null=True)
    role = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    zipcode = models.IntegerField(max_length=50, null=True)
    state = models.CharField(max_length=100, null=True)
    active = models.BooleanField(default=True)
    leave_count = models.IntegerField(null=True, default=0)
    on_leave = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
