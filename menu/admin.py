from django.contrib import admin
from .models import Dish, Category

admin.site.register(Category)
admin.site.register(Dish)