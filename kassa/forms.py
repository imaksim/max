from django import forms
from .models import *
class OperationNameForm(forms.ModelForm):
    name = forms.CharField(label="Имя")
    class Meta:
        model = OperationName
        fields = ['name']

class OperationNameMinusForm(forms.ModelForm):
    name = forms.CharField(label="Имя")
    class Meta:
        model = OperationNameMinus
        fields = ['name']
class SaleForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['payment', 'notice', 'total']
class OperationForm(forms.ModelForm):
    class Meta:
        model = Operations
        fields = ['operation_name', 'price', 'amount']

OperationFormSet = forms.modelformset_factory(Operations, form=OperationForm, extra=1)