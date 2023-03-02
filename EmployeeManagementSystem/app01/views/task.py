from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt


def task_list(request):
    return render(request, 'task_list.html')


@csrf_exempt
def task_ajax(request):
    return HttpResponse("success")
