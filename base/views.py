from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddEmployeeForm
from .models import *
from django.db.models import Q

# Create your views here.


def home(request):
    employees = Employee.objects.all().count()
    empOnLeave = Employee.objects.filter(on_leave=True).count()

    labels = ['Total Employees', 'Employees on leave']
    data = [employees, empOnLeave]

    context = {'employees': employees, 'empOnLeave': empOnLeave,
               'labels': labels, 'data': data}
    return render(request, 'base/home.html', context)


def view_employees(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    employees = Employee.objects.filter(
        Q(name__icontains=q) |
        Q(dob__icontains=q) |
        Q(doj__icontains=q) |
        Q(department__name__icontains=q) |
        Q(role__name__icontains=q) |
        Q(address__icontains=q) |
        Q(city__icontains=q) |
        Q(state__icontains=q) |
        Q(country__icontains=q) |
        Q(zipcode__icontains=q) |
        Q(leaves__icontains=q)
    )

    query = False
    if request.method == 'GET' and 'q' in request.GET:
        query = True

    employeesCount = employees.count()

    context = {'employees': employees,
               'employees_count': employeesCount, 'query': query}
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
            return redirect('addSuccess')
    context = {'form': form, 'Title': 'Create'}
    return render(request, 'base/add_employee.html', context)


def add_employee_success(request):
    message = 'Employee Added successfully ✅'
    return render(request, 'base/success.html', {'message': message})


def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = AddEmployeeForm(instance=employee)
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            obj = form.save(commit=False)
            if (obj.on_leave):
                obj.leaves += 1
            obj.save()
            return redirect(f'/employee/view/{pk}')
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
        return redirect('list')
    message = f"Are you sure you want to delete {employee.name}?"
    return render(request, 'base/confirm.html', {'message': message})


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
        return redirect(f'/employee/view/{pk}')

    message = f"Are you sure you want to change {employee.name}'s status to {status}?"

    context = {'message': message}
    return render(request, 'base/confirm.html', context)


def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    formatted_dob = employee.dob.strftime("%x")
    formatted_doj = employee.doj.strftime("%x")
    context = {'emp': employee, 'dob': formatted_dob, 'doj': formatted_doj}
    return render(request, 'base/employee_details.html', context)
