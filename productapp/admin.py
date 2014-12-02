from django.contrib import admin

# Register your models here.
from productapp.models import District, Community, Image, Product

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    list_filter = ['name',]
    search_fields = ['name',]
    list_per_page = 20

class CommunityAdmin(admin.ModelAdmin):
    list_display = ('name', 'district')
    list_filter = ['name', 'district']
    search_fields = ['name', 'district']
    list_per_page = 20

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url',)
    search_fields = ['name',]
    list_per_page = 20

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'datetime_available')
    list_filter = ['name', 'datetime_available']
    search_fields = ['name',]
    list_per_page = 20

admin.site.register(District, DistrictAdmin)
admin.site.register(Community, CommunityAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Product, ProductAdmin)