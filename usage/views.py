from django.shortcuts import render


def index(request):
    return render(request, 'usage/index.html')


def person_list(request):
    return render(request, 'usage/person_list.html')


def person_list_with_detail_href(request):
    return render(request, 'usage/person_list_with_detail_href.html')