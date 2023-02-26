from django.shortcuts import render, redirect
from app01 import models


# Create your views here.
def depart_list(request):
    depart_list = models.Department.objects.all()
    return render(request, 'depart_list.html',
                  {"depart_list": depart_list})


def depart_add(request):
    if request.method == "GET":
        return render(request, 'depart_add.html')

    depart_title = request.POST.get("title")
    models.Department.objects.create(title=depart_title)
    return redirect('/depart/list')


def depart_delete(request):
    # print(request.method)
    depart_id = request.GET.get("id")
    models.Department.objects.filter(id=depart_id).delete()
    return redirect('/depart/list')


def depart_edit(request, did):
    
    return render(request, 'depart_edit.html')
