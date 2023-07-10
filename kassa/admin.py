from django.contrib import admin
from .models import OperationName, OperationNameMinus, PaymentMethods, Operations, Sales


class OperationNameAdmin(admin.ModelAdmin):
    verbose_name = 'Операции'


# Register your models here.
admin.site.register(OperationName, OperationNameAdmin)
admin.site.register(OperationNameMinus)
admin.site.register(PaymentMethods)
admin.site.register(Operations)
admin.site.register(Sales)
