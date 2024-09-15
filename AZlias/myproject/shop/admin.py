from django.contrib import admin
from .models import *

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Number of extra empty image fields to show

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'is_available', 'created_at')
    search_fields = ('name', 'description', 'brand')
    list_filter = ('is_available', 'brand', 'color')
    inlines = [ProductImageInline]

admin.site.register(Products, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Color)

