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
from app01 import viewsHome
from app01.views import depart
from app01.views import user
from app01.views import pretty
from app01.views import admin
from app01.views import account

urlpatterns = [
    # home
    path('', viewsHome.home),
    # depart
    path('depart/list', depart.depart_list),
    path('depart/add', depart.depart_add),
    path('depart/delete', depart.depart_delete),
    path('depart/<int:did>/edit', depart.depart_edit),
    # user
    path('user/list', user.user_list),
    path('user/add', user.user_add),
    path('user/modelForm/add', user.user_modelform_add),
    path('user/delete', user.user_delete),
    path('user/<int:uid>/edit', user.user_modelform_edit),
    # pretty
    path('pretty/list', pretty.pretty_list),
    path('pretty/add', pretty.pretty_add),
    path('pretty/<int:pid>/delete', pretty.pretty_delete),
    path('pretty/<int:pid>/edit', pretty.pretty_edit),
    # admin
    path('admin/list', admin.admin_list),
    path('admin/add', admin.admin_add),
    path('admin/<int:aid>/edit', admin.admin_edit),
    path('admin/<int:aid>/delete', admin.admin_delete),
    path('admin/<int:aid>/reset', admin.admin_reset),
    # account
    path('account/login', account.login),
]
