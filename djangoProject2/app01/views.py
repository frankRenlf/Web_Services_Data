from django.shortcuts import render
from django.shortcuts import render, HttpResponse


# Create your views here.
def test1(request):
    return HttpResponse('hhhh')


def test2(request):
    return render(request, "user_list.html")
