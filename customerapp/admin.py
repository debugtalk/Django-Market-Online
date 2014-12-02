from django.contrib import admin

# Register your models here.
from customerapp.models import Customer, Order

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'community', 'address', 'status')
    list_filter = ['name', 'community', 'status']
    search_fields = ['name', 'community']
    list_per_page = 20

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'total_price', 'order_time', 'confirm_time', 'transaction_mode', 'status', 'remark')
    list_filter = ['customer', 'order_time', 'confirm_time', 'transaction_mode', 'status']
    search_fields = ['customer']
    list_per_page = 20

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)