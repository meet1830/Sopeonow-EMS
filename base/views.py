from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.


def home(request):
    return render(request, 'base/home.html')


def view_employees(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'base/view_employees.html', context)


def add_employee(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        doj = request.POST['doj']
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        address = request.POST['address']
        zipcode = request.POST['zipcode']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']

        new_employee = Employee(
            name=name, dob=dob, doj=doj, dept_id=dept, role_id=role, address=address, zipcode=zipcode, city=city, state=state, country=country)

        new_employee.save()
        return HttpResponse('Employee added Successfully')

    elif request.method == 'GET':
        context = {}
        return render(request, 'base/add_employee.html', context)

    else:
        return HttpResponse("An error occured. Please try again.")
