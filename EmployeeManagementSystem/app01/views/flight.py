from app01 import models
from app01.utils.Pagination import Pagination
from app01.modelForms.flightModelForm import FlightModelForm
from datetime import datetime
from rest_framework import generics
from app01.models import Department
from app01.serializers import MyModelSerializer
from django.shortcuts import render, redirect, HttpResponse
from app01 import models
from app01.utils.Pagination import Pagination


def flight_list(request):
    flight_union = models.Flight.objects.all()
    pagination = Pagination(request, flight_union)
    return render(request, 'flight_list.html',
                  {'flight_union': pagination.number_list, "page_list": pagination.page_list})


def flight_modelform_add(request):
    if request.method == "GET":
        user_null = FlightModelForm()
        return render(request, 'flightForm_add.html', {"flightForm": user_null})
    user_form = FlightModelForm(data=request.POST)
    if user_form.is_valid():
        user_form.save()
        return redirect('/flight/list')
    return render(request, 'flightForm_add.html', {"flightForm": user_form})


def flight_modelform_edit(request, uid):
    user = models.Flight.objects.filter(id=uid).first()
    if request.method == "GET":
        user_null = FlightModelForm(instance=user)
        return render(request, 'flightForm_edit.html', {"flightForm": user_null})
    user_form = FlightModelForm(data=request.POST, instance=user)
    if user_form.is_valid():
        user_form.save()
        return redirect('/flight/list')
    return render(request, 'flightForm_edit.html', {"flightForm": user_form})
    # return HttpResponse(uid)


def flight_delete(request):
    uid = request.GET.get("id")
    models.Flight.objects.filter(id=uid).delete()
    return redirect('/flight/list')


class FlightList(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        flight_union = models.Flight.objects.all()
        pagination = Pagination(request, flight_union)
        return render(request, 'flight_list.html',
                      {'flight_union': pagination.number_list, "page_list": pagination.page_list})

    def post(self, request, *args, **kwargs):
        uid = request.POST.get("fid")
        models.Flight.objects.filter(id=uid).delete()
        flight_union = models.Flight.objects.all()
        pagination = Pagination(request, flight_union)
        return render(request, 'flight_list.html',
                      {'flight_union': pagination.number_list, "page_list": pagination.page_list})


