from django.contrib import admin
from products.models import product, category


class productAdmin(admin.ModelAdmin):
    fieldsets = [
        ('name', {'fields': ['name']}),
        ('slug', {'fields': ['slug']}),
        ('description', {'fields': ['description']}),
        ('price', {'fields': ['price']}),
        ('category', {'fields': ['category']}),
    ]
    list_display = ('name', 'slug', 'price', 'category')
    search_fields = ["name"]


class categoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('name', {'fields': ['name']}),
        ('slug', {'fields': ['slug']}),
        ('description', {'fields': ['description']}),

    ]
    list_display = ('name', 'slug')
    search_fields = ["name"]


admin.site.register(category, categoryAdmin)
admin.site.register(product, productAdmin)
