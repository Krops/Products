from django.contrib import admin
from products.models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('name', {'fields': ['name']}),
        ('slug', {'fields': ['slug']}),
        ('description', {'fields': ['description']}),
        ('price', {'fields': ['price']}),
        ('category', {'fields': ['category']}),
    ]
    list_display = ('name', 'slug', 'price', 'category')
    search_fields = ["name"]


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('name', {'fields': ['name']}),
        ('slug', {'fields': ['slug']}),
        ('description', {'fields': ['description']}),

    ]
    list_display = ('name', 'slug')
    search_fields = ["name"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
