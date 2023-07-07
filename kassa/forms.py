from django import forms
from .models import *
class OperationNameForm(forms.ModelForm):
    name = forms.CharField(label="Имя")
    class Meta:
        model = OperationName
        fields = ['name']

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['payment', 'notice', 'total']
class OperationForm(forms.ModelForm):
    class Meta:
        model = Operations
        fields = ['operation_name', 'deb_cred', 'price', 'amount']

OperationFormSet = forms.modelformset_factory(Operations, form=OperationForm, extra=1)