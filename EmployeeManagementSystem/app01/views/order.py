from django.shortcuts import render, redirect
from app01 import models
from app01.utils.Pagination import Pagination
from app01.modelForms.OrderModelForm import OrderModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def order_list(request):
    form = OrderModelForm()
    return render(request, "order_list.html", {"form": form})


@csrf_exempt
def order_add(request):
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": form.errors})
