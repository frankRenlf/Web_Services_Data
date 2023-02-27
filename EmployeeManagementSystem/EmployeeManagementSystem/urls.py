"""EmployeeManagementSystem URL Configuration

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
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
    # home
    path('', views.home),
    # depart
    path('depart/list', views.depart_list),
    path('depart/add', views.depart_add),
    path('depart/delete', views.depart_delete),
    path('depart/<int:did>/edit', views.depart_edit),
    # user
    path('user/list', views.user_list),
    path('user/add', views.user_add),
    path('user/modelForm/add', views.user_modelform_add),
    path('user/delete', views.user_delete),
    path('user/<int:uid>/edit', views.user_modelform_edit),
    # pretty
    path('pretty/list', views.pretty_list),
    path('pretty/add', views.pretty_add),
    path('pretty/<int:pid>/delete', views.pretty_delete),
    path('pretty/<int:pid>/edit', views.pretty_edit),
]
