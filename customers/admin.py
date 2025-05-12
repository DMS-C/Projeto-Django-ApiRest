from django.contrib import admin
from customers.models import Customer
# Register your models here.


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf_cnpj', 'contact', 'address')
    search_fields = ('name', 'cpf_cnpj')
    list_filter = ('name',)