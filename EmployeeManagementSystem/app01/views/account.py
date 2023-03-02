from django.shortcuts import render, redirect
from app01 import models
from app01.modelForms.LoginModelForm import LoginModelForm


def login(request):
    if request.method == "GET":
        form = LoginModelForm()
        return render(request, 'login.html', {"form": form})
    admin = models.Admin.objects.filter(name=request.POST.get("name")).first()
    form = LoginModelForm(data=request.POST, instance=admin)
    if form.is_valid():
        request.session["info"] = {"id": admin.id, "name": admin.name}
        print(request.session)
        return redirect('/admin/list')
    return render(request, 'login.html', {"form": form})