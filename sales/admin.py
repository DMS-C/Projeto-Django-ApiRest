from django.contrib import admin
from sales.models import Sale

# Register your models here.

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('customer', 'car', 'sale_date', 'value', 'payment_method')
    search_fields = ('customer__name', 'car__model', 'payment_method')
    list_filter = ('sale_date', 'payment_method')
    