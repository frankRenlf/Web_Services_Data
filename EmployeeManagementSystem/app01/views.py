from django.shortcuts import render, redirect, HttpResponse
from app01 import models
from django import forms


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


class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", "gender", "salary", "create_time", "depart"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control"}


def user_list(request):
    user_union = models.UserInfo.objects.all()
    return render(request, 'user_list.html', {'user_union': user_union})


def user_add(request):
    if request.method == "GET":
        departs = models.Department.objects.all()
        gender_choices = models.UserInfo.gender_choices
        return render(request, 'user_add.html', {"departs": departs, "gender_choices": gender_choices})
    user = models.UserInfo
    user.name = request.POST.get("name")
    user.password = request.POST.get("password")
    user.age = request.POST.get("age")
    user.gender = request.POST.get("gender")
    user.salary = request.POST.get("salary")
    user.create_time = request.POST.get("create_time")
    user.depart.id = request.POST.get("depart_id")
    models.UserInfo.objects.create(name=user.name, password=user.password, age=user.age, gender=user.gender,
                                   salary=user.salary,
                                   create_time=user.create_time,
                                   depart_id=user.depart.id)
    return redirect('/user/list')


def user_modelform_add(request):
    if request.method == "GET":
        user_null = UserModelForm()
        return render(request, 'userForm_add.html', {"userForm": user_null})
    user_form = UserModelForm(data=request.POST)
    if user_form.is_valid():
        user_form.save()
        return redirect('/user/list')
    return render(request, 'userForm_add.html', {"userForm": user_form})


def user_modelform_edit(request, uid):
    user = models.UserInfo.objects.filter(id=uid).first()
    if request.method == "GET":
        user_null = UserModelForm(instance=user)
        return render(request, 'userForm_edit.html', {"userForm": user_null})
    user_form = UserModelForm(data=request.POST, instance=user)
    if user_form.is_valid():
        user_form.save()
        return redirect('/user/list')
    return render(request, 'userForm_edit.html', {"userForm": user_form})
    # return HttpResponse(uid)


def user_delete(request):
    uid = request.GET.get("id")
    models.UserInfo.objects.filter(id=uid).delete()
    return redirect('/user/list')
