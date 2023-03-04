from django.shortcuts import render, redirect
from app01 import models
from app01.utils.Pagination import Pagination
from app01.modelForms.OrderModelForm import OrderModelForm


def order_list(request):
    form = OrderModelForm()
    return render(request, "order_list.html", {"form": form})
