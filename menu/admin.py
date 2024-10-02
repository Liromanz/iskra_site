from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'additional_info', 'picture')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_editable = ('price', 'picture')

