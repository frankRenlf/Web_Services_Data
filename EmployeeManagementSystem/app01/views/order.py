from django.shortcuts import render, redirect
from app01 import models
from app01.utils.Pagination import Pagination
from app01.modelForms.PrettyModelForm import PrettyModelForm


def order_list(request):
    return render(request, "order_list.html")
