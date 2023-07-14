from django.contrib import admin
from .models import OperationName, PaymentMethods, Sale, Operation


class OperationNameAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'type']
    list_filter = ['type']
    search_fields = ['pk', 'name']

class OperationInline(admin.TabularInline):
    model = Operation

class SaleAdmin(admin.ModelAdmin):
    inlines = [OperationInline]
# Register your models here.
admin.site.register(OperationName, OperationNameAdmin)
admin.site.register(Operation)
admin.site.register(PaymentMethods)
admin.site.register(Sale, SaleAdmin)
