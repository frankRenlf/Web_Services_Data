import json

import requests
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


class PaymentProvider(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, *args, **kwargs):
        oid = request.GET.get("oid")
        aid = request.GET.get("aid")
        ta = request.GET.get("ta")
        al = request.GET.get("al")
        api = request.GET.get("api")
        dm = request.GET.get("dm")
        url = 'http://bamboo.pythonanywhere.com/{}/'.format(api)
        print(url)
        params = {
            "orderId": oid,
            "AID": aid,
            "totalAmount": ta,
            "airline": al,
        }
        response = requests.post(url, data=params)
        return JsonResponse(response.json())

    def post(self, request, *args, **kwargs):
        return JsonResponse()
