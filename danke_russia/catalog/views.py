# Create your views here. Для хранения контроллеров текущего приложения
from django.http import HttpResponse
from django.shortcuts import render

# Функция представление для страницы Products
def catalog(request): # request - ссылка на HttpRequest
    return HttpResponse("Страница приложения Catalog") # HttpResponse(х), х - содержимое главное страницы

def product(request): # request - ссылка на HttpRequest
    return HttpResponse("Страница приложения Catalog")