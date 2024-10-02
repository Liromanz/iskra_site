from django.shortcuts import render
from .models import *


# Create your views here.


def index(request):
    dishes = Dish.objects.all()
    return render(request, 'main_menu.html', context={"dishes": dishes})
