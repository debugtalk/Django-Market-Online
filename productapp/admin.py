from django.contrib import admin

# Register your models here.
from productapp.models import Area, Image, Product

class AreaAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    list_filter = ['code', 'name']
    search_fields = ['code', 'name']
    list_per_page = 20

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url',)
    search_fields = ['name', 'url',]
    list_per_page = 20

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'datetime_available')
    list_filter = ['name', 'datetime_available']
    search_fields = ['name',]
    list_per_page = 20

admin.site.register(Area, AreaAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Product, ProductAdmin)