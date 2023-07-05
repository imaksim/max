from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView

from .models import OperationName


# Create your views here.


def operation_list(request):
    operations = OperationName.objects.all()
    return render(request, 'operation.html', {'operations': operations})

class OperationNameDeleteView(DeleteView):
    model = OperationName
    success_url = reverse_lazy('operation_list')  # URL, на который будет перенаправлен пользователь после успешного удаления

class OperationNameUpdateView(UpdateView):
    model = OperationName
    fields = ['name', 'description']  # поля, которые будут обновлены
    template_name_suffix = '_update_form'  # Django автоматически будет искать шаблон с именем <model>_update_form.html
    success_url = reverse_lazy('operation_list')  # URL, на ко

