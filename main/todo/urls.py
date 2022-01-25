from unicodedata import name
from django.urls import URLPattern, path
from .views import *

urlpatterns = [
    path('', home,name="home-todo"),
    path('delete/<str:pk>',delete, name = "delete-todo")
]