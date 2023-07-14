from django.db import models

# Create your models here.
from django.db import models
from django.core import validators
from django.conf import settings



class OperationName(models.Model):
    name = models.CharField(max_length=255)
    OPERATION_TYPES = [
        ('plus', 'Plus'),
        ('minus', 'Minus'),
    ]

    type = models.CharField(
        max_length=5,
        choices=OPERATION_TYPES,
        default='plus',
    )

    class Meta:
        db_table = "OperationName"
        verbose_name = 'Имя операции'
        verbose_name_plural = 'Имена операций'

    def __str__(self):
         return f"{self.name}"

class PaymentMethods(models.Model):
    name = models.CharField(max_length=32)


    class Meta:
        db_table = "payment_methods"
    def __str__(self):
         return f"{self.name}"
class Operation(models.Model):
    sale = models.ForeignKey('Sale', on_delete=models.PROTECT, null=True)
    operation_name = models.ForeignKey(OperationName, on_delete=models.PROTECT, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField(validators=[validators.MinValueValidator(0)])
    def __str__(self):
         return f"{self.operation_name} {self.price} {self.amount}"



    class Meta:
         db_table = "operations"

class Sale(models.Model):
    # operations = models.ManyToManyField(Operation, blank=False)
    date = models.DateTimeField(auto_now_add=True,)
    update_date = models.DateTimeField(auto_now_add=True,)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True)
    # user = models.CharField(max_length=32, default='admin')
    total = models.DecimalField(max_digits=15, decimal_places=2, validators=[validators.MinValueValidator(0)])
    payment = models.ForeignKey(PaymentMethods, on_delete=models.PROTECT, null=True)
    notice = models.TextField(null=True)
    def __str__(self):
         return f"{self.date}"
    class Meta:
        db_table = "sales"


