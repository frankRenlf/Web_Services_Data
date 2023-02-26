from django.shortcuts import render
from app01 import models


# Create your views here.
def depart_list(request):
    depart_list = models.Department.objects.all()
    return render(request, 'depart_list.html',
                  {"depart_list": depart_list})


def depart_add(request):
    depart_title = request.POST.get("title")
    models.Department.objects.create(title=depart_title)
    return render(request, 'depart_list.html',
                  {"depart_list": depart_list})