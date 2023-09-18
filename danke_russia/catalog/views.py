# Create your views here. Для хранения контроллеров текущего приложения
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Функция представление для страницы Products
def catalog(request): # request - ссылка на HttpRequest
    return render(request, 'catalog/catalog.html', {"title": "Подоконники Danke"}) # render - шаблонизатор django

def about(request): # request - ссылка на HttpRequest
    return render(request, 'catalog/about.html')

def contacts(request): # request - ссылка на HttpRequest
    return render(request, 'catalog/contacts.html')


def product(request, product):
    return HttpResponse(f'<h1>{product}</h1>')


# Обработчик ошибки 404 Not Found
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')