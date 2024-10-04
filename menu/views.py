from django.shortcuts import render
from .models import *


# Create your views here.


def index(request):
    menu = []
    categories = DishCategory.objects.all()

    for category in categories:
        dishes_in_category = Dish.objects.filter(category=category)
        if len(dishes_in_category) > 0:
            menu.append({"category":category, "dishes": dishes_in_category})

    dishes_in_category = Dish.objects.filter(category=None)
    if len(dishes_in_category) > 0:
        menu.append({"category": "Общее", "dishes": dishes_in_category})
    return render(request, 'main_menu.html', context={"menu": menu})
