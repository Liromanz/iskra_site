from django.db import models

# Create your models here.


class DishCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название категории", null=False)

    def __str__(self):
        return f"{self.name}"

    class Meta():
        verbose_name = "Категория блюда"
        verbose_name_plural = "Категории блюд"


class Dish(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название блюда", null=False)
    category = models.ForeignKey( DishCategory, models.SET_NULL, null=True, default=None, blank=True, verbose_name="Категория")
    price = models.IntegerField(verbose_name="Цена в рублях", null=False)
    additional_info = models.CharField(max_length=20, verbose_name="Количество (гр, шт, мл)", null=True, blank=True )
    compound = models.TextField(verbose_name="Состав", null=True, blank=True)
    picture = models.ImageField(verbose_name="Фото блюда", null=True, upload_to='dishes/', default="/")

    def __str__(self):
        return f"{self.name} - {self.price}"
    class Meta():
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"

