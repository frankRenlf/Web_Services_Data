from django.shortcuts import render, redirect
from app01 import models
from app01.utils.Pagination import Pagination
from app01.modelForms.OrderModelForm import OrderModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime


def chart_list(request):
    return render(request, "chat_list.html")


def chart_bar(request):
    legend = ['1', '2']
    series = [{
        'name': '1',
        'type': 'bar',
        'data': [5, 20, 36, 10, 10, 20, 60]
    }, {
        'name': '2',
        'type': 'bar',
        'data': [20, 60, 5, 20, 36, 10, 10]
    }]
    xAxis = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']
    result = {
        "status": True,
        "data": {
            "legend": legend,
            "series": series,
            "xAxis": xAxis
        }
    }
    return JsonResponse(result)
