from django.urls import path
import menu.views as v

urlpatterns = [
    path('', v.index, name='index'),
]
