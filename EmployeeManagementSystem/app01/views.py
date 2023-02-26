from django.shortcuts import render
from app01 import models


# Create your views here.
def depart_list(request):
    depart_list = models.Department.objects.all()
    return render(request, 'depart_list.html',
                  {"depart_list": depart_list})
