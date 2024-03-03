from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
# функции представления нашего сайта


def index(request):
    return HttpResponse('Страница сайта Courses')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
