from django.db import models

# Create your models here.
from django.db import models
from django.core import validators


class Stuff(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField(max_length=254)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "stuff"
    def __str__(self):
         return  f"{self.name}"


class OperationName(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "OperationName"

    def __str__(self):
         return f"{self.id})  {self.name}"

class PaymentMethods(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        db_table = "payment_methods"

class Operations(models.Model):
    fk_name_of_product = models.ForeignKey(OperationName, on_delete=models.PROTECT, null=True)
    deb_cred = models.BooleanField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField(validators=[validators.MinValueValidator(0)])


    class Meta:
        db_table = "operations"

class Sales(models.Model):
    sell_id = models.IntegerField(validators=[validators.MinValueValidator(0)])
    date = models.DateTimeField(auto_now_add=True,)
    update_date = models.DateTimeField(auto_now_add=True,)
    fk_stuff = models.ForeignKey(Stuff, on_delete=models.PROTECT, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=2, validators=[validators.MinValueValidator(0)])
    fk_payment = models.ForeignKey(PaymentMethods, on_delete=models.PROTECT, null=True)
    notice = models.TextField(null=True)

    class Meta:
        db_table = "sales"