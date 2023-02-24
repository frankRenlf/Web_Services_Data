from django.shortcuts import render
from django.shortcuts import render, HttpResponse


# Create your views here.
def test1(request):
    return HttpResponse('hhhh')


def test2(request):
    return render(request, "user_list.html")


def test3(request):
    name = "frank"
    list1 = [1, 2, 3]
    user_info = {
        "address": 'hz',
        "age": 23
    }
    user_info_list = [
        {"name": 'f', "address": 'hz', "age": 23},
        {"name": 'f', "address": 'hz', "age": 23},
        {"name": 'f', "address": 'hz', "age": 23},
    ]
    return render(request,
                  "user_list.html",
                  {
                      "d1": name,
                      "l1": list1,
                      "ui": user_info,
                      "ui_list": user_info_list
                  })


# https://www.chinaunicomglobal.com/hk/unicmsApi/door/hkHotNews/hkHotNewslist
import requests


def test4(request):
    return render(request, "news.html", )
