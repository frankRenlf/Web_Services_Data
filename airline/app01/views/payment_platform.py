import json
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from app01 import models
from app01.utils.Pagination import Pagination
from app01.modelForms.flightModelForm import FlightModelForm
from datetime import datetime
from rest_framework import generics
from app01.models import Department, Flight
from app01.serializers import MyModelSerializer
from django.shortcuts import render, redirect, HttpResponse
from app01 import models
from app01.utils.Pagination import Pagination


class PaymentPlatform(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, *args, **kwargs):
        data_list = models.payment_method.objects.all()
        pagination = Pagination(request, data_list)
        return render(request, 'payment_platform.html',
                      {'data_list': pagination.number_list, "page_list": pagination.page_list})
