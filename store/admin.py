# store/admin.py
from django.contrib import admin
from .models import Product, Review, Wishlist

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'size', 'color', 'popularity')
    search_fields = ('name', 'size', 'color')
    list_filter = ('size', 'color')

admin.site.register(Product, ProductAdmin)
admin.site.register(Review)
admin.site.register(Wishlist)

