from django.urls import path

from .views import *
# Маршруты по определенным ссылкам на представление

urlpatterns = [
    path('', catalog, name='home'), # home - имя маршрута по которому можно обращаться к пути
    path('<slug:product>/', product)
    ]