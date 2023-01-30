from django.db import models


class Category(models.Model):
    """
    Returns category for the dishes
    """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Dish(models.Model):
    """
    Returns dishes and their details
    """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=False, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    featured = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name