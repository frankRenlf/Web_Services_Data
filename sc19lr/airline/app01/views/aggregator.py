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


class Aggregator(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, *args, **kwargs):
        url = 'http://bamboo.pythonanywhere.com/bookingStatus/'
        response = requests.get(url)
        return JsonResponse(response.json())

    def post(self, request, *args, **kwargs):
        return JsonResponse()
