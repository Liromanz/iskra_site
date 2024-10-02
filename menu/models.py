from django.db import models

# Create your models here.

class Dish(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название блюда", null=False)
    price = models.FloatField(verbose_name="Цена в рублях", null=False)
    additional_info = models.CharField(max_length=20, verbose_name="Количество (гр, шт, мл)", null=True)
    compound = models.TextField(verbose_name="Состав", null=True)
    picture = models.ImageField(verbose_name="Фото блюда", null=True, upload_to='menu/img/dishes/')

    class Meta():
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"

