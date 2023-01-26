"""Sopeonow_EMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('employee/view', views.view_employees, name="view"),

    path('employee/add', views.add_employee, name="add"),
    path('employee/ajax/load-roles/', views.load_roles,
         name='ajax_load_roles'),  # AJAX

    path('employee/update/<int:pk>/', views.update_employee, name='update'),

    path('employee/delete/<int:pk>/', views.delete_employee, name='delete'),

    path('employee/leave/<int:pk>/', views.leave_status, name='leave'),
]
