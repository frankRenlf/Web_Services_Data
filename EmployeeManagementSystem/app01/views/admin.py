from django.shortcuts import render, redirect
from app01 import models
from app01.utils.Pagination import Pagination
from app01.modelForms.AdminModelForm import AdminModelForm


def admin_list(request):
    search = "name"
    name_txt = request.GET.get(search)
    name_txt = name_txt if name_txt is not None else ''
    page_size = 3
    data_dict = {}
    if name_txt:
        data_dict[search + "__contains"] = name_txt
    data_list = models.Admin.objects.filter(**data_dict)
    sub = 2
    pagination = Pagination(request, data_list, search, page_size, "index", sub)

    return render(request, 'admin_list.html',
                  {"number_list": pagination.number_list, "page_list": pagination.page_list,
                   search: "" if pagination.search_query is None else pagination.search_query})
