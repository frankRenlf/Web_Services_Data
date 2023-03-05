from django.shortcuts import render, redirect
from app01 import models
from app01.utils.Pagination import Pagination
from app01.modelForms.OrderModelForm import OrderModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime


def upload_list(request):
    if request.method == 'GET':
        return render(request, 'upload_list.html')
    print(request.POST)
    print(request.FILES)
    return render(request, 'upload_list.html')
