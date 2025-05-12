from django.contrib import admin
from cars.models import Car, Brand
# Register your models here.

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'model_year', 'plate', 'value', 'status', 'entry_date')
    search_fields = ('model', 'brand__name', 'plate')
    list_filter = ('brand', 'model_year', 'status')
    list_editable = ('value',)
    ordering = ('-entry_date',)