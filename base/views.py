from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
    return render(request, 'base/home.html')


def view_employees(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'base/view_employees.html', context)
