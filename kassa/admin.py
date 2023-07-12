from django.contrib import admin
from .models import OperationName, OperationNameMinus, PaymentMethods, Sale, Operation


class OperationNameAdmin(admin.ModelAdmin):
    verbose_name = 'Операции'


# Register your models here.
admin.site.register(OperationName, OperationNameAdmin)
admin.site.register(OperationNameMinus)
admin.site.register(Operation)
admin.site.register(PaymentMethods)
admin.site.register(Sale)
