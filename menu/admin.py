from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(DishCategory)

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'picture')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_editable = ('category', 'price', 'picture')


