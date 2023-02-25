from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect


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
    res = requests.get("https://api.github.com/users?since=2", verify=False)
    data_list = res.json()
    # print(data_list)
    print(request.method)
    return render(request, "news.html", {"dl": data_list})


def test5(request):
    # print(data_list)
    print(request.GET)
    print(request.POST)
    # return render(request, "req.html")
    return redirect("https://www.bing.com")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    print(request.POST)
    if request.POST.get("username") == "f" \
            and request.POST.get("password") == "123":
        return HttpResponse("success")

    return render(request, "login.html", {"error": "wrong account"})


def insert(request):

    return render(request, "user_info.html", {"data":})
