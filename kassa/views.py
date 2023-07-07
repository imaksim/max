from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, CreateView
from django.views.generic.list import ListView
from .models import OperationName, Sales, Operations
from .forms import OperationNameForm, SaleForm, OperationFormSet


# Create your views here.


def operation_name_list(request):
    operations = OperationName.objects.all()
    my_value = request.session.get('form_data', '')
    return render(request, 'operation.html', {'operations': operations, 'my_value': my_value})

def add_operation_name(request):
    if request.method == 'POST':
        form = OperationNameForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['form_data'] = ''
            return redirect('operation_list')
        else:
            request.session['form_data'] = form.errors['name'][0]
            return redirect('operation_list')

def edit_operation_name(request, pk):
    operation = get_object_or_404(OperationName, pk=pk)
    if request.method == 'POST':
        form = OperationNameForm(request.POST, instance=operation)
        if form.is_valid():
            form.save()
            return redirect('operation_list')
    else:
        form = OperationNameForm(instance=operation)
    return render(request, 'edit_operation_name.html', {'form': form, 'operation': operation})
def delete_operation_name(request):
    if request.method == 'POST':
        operation_name_ids = request.POST.getlist('selected_item')
        OperationName.objects.filter(id__in=operation_name_ids).delete()
    return redirect('operation_list')
def add_sale(request):
    if request.method == 'POST':
        form=SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sale_list')
        else:
            request.session['form_data'] = form.errors
            return redirect('sale_list')
def sale_list(request):
    sales = Sales.objects.all()
    return render(request, 'sales.html', {'sales': sales})
def sale(request):
    form = SaleForm()
    formset  = OperationFormSet(queryset=Operations.objects.none())
    context = {'form': form, 'sale': '', 'formset': formset}
    return render(request, 'sale.html', context)

def add_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        formset = OperationFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            sale = form.save()
            operations = formset.save(commit=False)
            for operation in operations:
                operation.sale = sale
                operation.save()
            return redirect('sale_list')

