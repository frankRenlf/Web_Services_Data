import math

from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from app01 import models
from django.utils.safestring import mark_safe
from utils.Pagination import Pagination

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
    mobile_txt = request.GET.get("mobile")
    mobile_txt = mobile_txt if mobile_txt is not None else ''
    page_index = int(request.GET.get('index', 1) if request.GET.get('index', 1) != '' else 1)
    page_size = 3
    data_start = (page_index - 1) * page_size
    data_end = page_index * page_size
    data_dict = {}

    if mobile_txt:
        data_dict["mobile__contains"] = mobile_txt
    # print(data_dict)
    data_list = models.PrettyNumber.objects.filter(**data_dict).order_by("-level")
    number_list = data_list[data_start: data_end]
    data_size = math.ceil(data_list.count() / page_size)
    page_list = []
    sub = 2

    pagination = Pagination(request, data_list, page_size, "index", sub)
    
    first = max(page_index - sub, 1)

    page_list.append('<li class=""><a href="?index={}&mobile={}" aria-label="Previous">'
                     '<span aria-hidden="true">First</span></a></li>'.format(1, mobile_txt))
    if page_index == 1:
        page_list.append('<li class="disabled"><a href="?mobile={}" aria-label="Previous">'
                         '<span aria-hidden="true">«</span></a></li>'.format(mobile_txt))
    else:
        page_list.append('<li class=""><a href="?index={}&mobile={}" aria-label="Previous">'
                         '<span aria-hidden="true">«</span></a></li>'.format(page_index - 1, mobile_txt))
    end = min(page_index + sub, data_size)
    for i in range(first, end + 1):
        if i == page_index:
            page_list.append('<li class=active><a href="?index={}&mobile={}">{}</a></li>'.format(i, mobile_txt, i))
        else:
            page_list.append('<li><a href="?index={}&mobile={}">{}</a></li>'.format(i, mobile_txt, i))
    if page_index == data_size:
        page_list.append('<li class="disabled"><a href="?index={}&mobile={}" aria-label="Next">'
                         '<span aria-hidden="true">»</span></a></li>'.format(page_index, mobile_txt))
    else:
        page_list.append('<li class=""><a href="?index={}&mobile={}" aria-label="Next">'
                         '<span aria-hidden="true">»</span></a></li>'.format(page_index + 1, mobile_txt))
    page_list.append('<li class=""><a href="?index={}&mobile={}" aria-label="Previous">'
                     '<span aria-hidden="true">End</span></a></li>'.format(data_size, mobile_txt))
    page_list.append("""
            <form method="get">
            <div class="input-group" style="width: 200px">
                <input type="text" name="index" class="form-control" placeholder="page number">
                <span class="input-group-btn">
                <button class="btn btn-default" type="submit">jump</button>
            </span>
            </div>
        </form>
        """)
    page_str = mark_safe("".join(page_list))
    return render(request, 'pretty_list.html',
                  {"number_list": number_list, "page_list": page_str,
                   "mobile": "" if mobile_txt is None else mobile_txt})


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
