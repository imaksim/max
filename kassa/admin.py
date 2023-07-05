from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Stuff)
admin.site.register(OperationName)
admin.site.register(PaymentMethods)
admin.site.register(Operations)
admin.site.register(Sales)