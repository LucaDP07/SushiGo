from django.contrib import admin
from .models import Dish, Category


class DishAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )


ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

admin.site.register(Dish, DishAdmin)
admin.site.register(Category, CategoryAdmin)