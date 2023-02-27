from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from app01 import models

""" create depart operations """


def home(request):
    return render(request, 'layout.html')


# Create your views here.
""" create depart operations """


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


""" create userinfo operations """


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


""" create prettyNumber operations """


class PrettyModelForm(forms.ModelForm):
    class Meta:
        model = models.PrettyNumber
        fields = ["mobile", "price", "level", "status"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control"}

    def clean_mobile(self):
        mobile_txt = self.cleaned_data["mobile"]
        pid = self.instance.pk
        if models.PrettyNumber.objects.filter(mobile=mobile_txt).exclude(id=pid).exists():
            raise ValidationError("Number already exists")
        if len(mobile_txt) != 11:
            raise ValidationError("Length must be 11")
        return mobile_txt


def pretty_list(request):
    number_list = models.PrettyNumber.objects.all().order_by("-level")
    return render(request, 'pretty_list.html', {"number_list": number_list})


def pretty_add(request):
    if request.method == "GET":
        pretty_null = PrettyModelForm()
        return render(request, 'prettyForm_add.html', {"prettyForm": pretty_null})
    pretty_form = PrettyModelForm(data=request.POST)
    if pretty_form.is_valid():
        pretty_form.save()
        return redirect('/pretty/list')
    return render(request, 'prettyForm_add.html', {"prettyForm": pretty_form})


def pretty_delete(request, pid):
    models.PrettyNumber.objects.filter(id=pid).first().delete()
    return redirect('/pretty/list')


def pretty_edit(request, pid):
    pretty = models.PrettyNumber.objects.filter(id=pid).first()
    if request.method == "GET":
        pretty_null = PrettyModelForm(instance=pretty)
        return render(request, 'prettyForm_edit.html', {"prettyForm": pretty_null})
    pretty_form = PrettyModelForm(data=request.POST, instance=pretty)
    if pretty_form.is_valid():
        pretty_form.save()
        return redirect('/pretty/list')
    return render(request, 'prettyForm_edit.html', {"prettyForm": pretty_form})
