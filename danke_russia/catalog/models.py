# Файл для хранения ORM моделей/представление данных из базы данных
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='product_photos/', blank=True, null=True, verbose_name='Фото')
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель')
    color = models.CharField(max_length=50, blank=True, verbose_name='Цвет')
    material = models.CharField(max_length=50, blank=True, verbose_name='Материал')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Себестоимость')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    width = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True, verbose_name='Ширина')
    length = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True, verbose_name='Длина')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')

    # self - ссылка на текущий экземпляр класса product
    def __str__(self):
        return self.title