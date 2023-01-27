from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import AddEmployeeForm
from .models import *

# Create your views here.


def home(request):
    employees = Employee.objects.all().count()
    emp_on_leave = Employee.objects.filter(on_leave=True).count()
    context = {'employees': employees, 'emp_on_leave': emp_on_leave}
    return render(request, 'base/home.html', context)


def view_employees(request):
    employees = Employee.objects.all()
    employeesCount = employees.count()
    context = {'employees': employees, 'employees_count': employeesCount}
    return render(request, 'base/view_employees.html', context)


def add_employee(request):
    form = AddEmployeeForm()
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            if (obj.on_leave == True):
                obj.leaves += 1
            obj.save()
            return redirect('view')
    context = {'form': form, 'Title': 'Add'}
    return render(request, 'base/add_employee.html', context)


def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = AddEmployeeForm(instance=employee)
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            obj = form.save(commit=False)
            if (obj.on_leave == True):
                obj.leaves += 1
            obj.save()
            return redirect('view')
    context = {'form': form, 'Title': 'Edit'}
    return render(request, 'base/add_employee.html', context)


# AJAX
def load_roles(request):
    department_id = request.GET.get('department_id')
    roles = Role.objects.filter(department_id=department_id).all()
    return render(request, 'base/role_dropdown_list_options.html', {'roles': roles})


def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('view')
    return render(request, 'base/delete.html', {'obj': employee})


def leave_status(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    status = ''
    if employee.on_leave:
        status = 'At work'
    else:
        status = 'On leave'

    if request.method == 'POST':
        if employee.on_leave:
            employee.on_leave = False
        else:
            employee.leaves += 1
            employee.on_leave = True

        employee.save()
        return redirect('view')

    context = {'obj': employee, 'status': status}
    return render(request, 'base/leave_status.html', context)
