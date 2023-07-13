from django import forms
from .models import *
class OperationNameForm(forms.ModelForm):
    name = forms.CharField(label="Имя")
    class Meta:
        model = OperationName
        fields = ['name']


class SaleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Извлекаем пользователя из kwargs
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.user  # Сохраняем текущего пользователя
        if commit:
            instance.save()
        return instance
    class Meta:
        model = Sale
        fields = ['payment', 'notice', 'total']
class OperationForm(forms.ModelForm):
    class Meta:

        model = Operation
        fields = ['operation_name', 'price', 'amount']

OperationFormSet = forms.modelformset_factory(Operation, form=OperationForm, extra=1)