from django.shortcuts import render, redirect
from app01 import models


# Create your views here.
def depart_list(request):
    depart_union = models.Department.objects.all()
    return render(request, 'depart_list.html',
                  {"depart_union": depart_union})


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
    if request.method == "GET":
        title = models.Department.objects.filter(id=did).all()[0].title
        return render(request, 'depart_edit.html', {"title": title})
    title = request.POST.get("title")
    models.Department.objects.filter(id=did).update(title=title)
    return redirect('/depart/list')


def user_list(request):
    user_union = models.UserInfo.objects.all()
    return render(request, 'user_list.html', {'user_union': user_union})


def user_add(request):
    if request.method == "GET":
        return render(request, 'user_add.html')

    depart_title = request.POST.get("title")
    models.Department.objects.create(title=depart_title)
    return redirect('/user/list')


def user_delete(request):
    return redirect('/user/list')


def user_edit(request, uid):
    # if request.method == "GET":
    #     title = models.Department.objects.filter(id=uid).all()[0].title
    #     return render(request, 'depart_edit.html', {"title": title})
    # title = request.POST.get("title")
    # models.Department.objects.filter(id=did).update(title=title)
    return redirect('/user/list')
