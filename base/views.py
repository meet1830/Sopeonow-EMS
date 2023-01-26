from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import AddEmployeeForm
from .models import *

# Create your views here.


def home(request):
    return render(request, 'base/home.html')


def view_employees(request):
    employees = Employee.objects.all()
    employees_count = employees.count()
    context = {'employees': employees, 'employees_count': employees_count}
    return render(request, 'base/view_employees.html', context)


def add_employee(request):
    form = AddEmployeeForm()
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view')
    return render(request, 'base/add_employee.html', {'form': form})


def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = AddEmployeeForm(instance=employee)
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('view')
    return render(request, 'base/add_employee.html', {'form': form})


# AJAX
def load_roles(request):
    department_id = request.GET.get('department_id')
    roles = Role.objects.filter(department_id=department_id).all()
    return render(request, 'base/role_dropdown_list_options.html', {'roles': roles})
