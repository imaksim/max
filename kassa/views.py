from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, CreateView
from django.views.generic.list import ListView
from .models import OperationName, Sale, OperationNameMinus, Operation
from .forms import OperationNameForm, SaleForm, OperationNameMinusForm, OperationFormSet


# Create your views here.
def operation_name_minus_list(request):
    operations_minus = OperationNameMinus.objects.all()
    my_value = request.session.get('form_data', '')
    return render(request, 'operation_minus.html', {'operations_minus': operations_minus, 'my_value': my_value})

def add_operation_name_minus(request):
    if request.method == 'POST':
        form = OperationNameMinusForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['form_data'] = ''
            return redirect('operation_minus_list')
        else:
            request.session['form_data'] = form.errors['name'][0]
            return redirect('operation_minus_list')

def edit_operation_name_minus(request, pk):
    operation_minus = get_object_or_404(OperationNameMinus, pk=pk)
    if request.method == 'POST':
        form = OperationNameForm(request.POST, instance=operation_minus)
        if form.is_valid():
            form.save()
            return redirect('operation_minus_list')
    else:
        form = OperationNameMinusForm(instance=operation_minus)
    return render(request, 'edit_operation_name_minus.html', {'form': form, 'operation_minus': operation_minus})
def delete_operation_name_minus(request):
    if request.method == 'POST':
        operation_name_minus_ids = request.POST.getlist('selected_item')
        OperationNameMinus.objects.filter(id__in=operation_name_minus_ids).delete()
    return redirect('operation_minus_list')
############################################################################################################
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

def sale_list(request):
    sales = Sale.objects.all()
    return render(request, 'sales.html', {'sales': sales})
def sale(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    # sale=Sale.objects.all()
    # form = SaleForm()
    # formset  = OperationFormSet(queryset=Operations.objects.none())
    # context = {'form': form, 'sale': '', 'formset': formset}
    return render(request, 'sale.html', {'sale': sale})

def add_sale(request):
    if request.method == 'GET':
        form = SaleForm()
        formset  = OperationFormSet(queryset=Operation.objects.none())
        context = {'form': form, 'sale': '', 'formset': formset}
        return render(request, 'add_sale.html', context)
    if request.method == 'POST':
        form = SaleForm(request.POST)
        formset = OperationFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            new_sale = form.save()
            operations = formset.save(commit=False)
            for operation in operations:
                operation.sale = new_sale  # set the sale before saving
                operation.save()  # Save each operation first
            return redirect('sale_list')
        else:
            request.session['form_data'] = form.errors
            return redirect('sale_list')
