from django.shortcuts import render, redirect, get_object_or_404
from .models import Sintoma, Tratamento
from .forms import SintomaForm, TratamentoForm
from collections import defaultdict

def home(request):
    sintomas = Sintoma.objects.all().order_by('-data', '-horario')
    tratamentos = Tratamento.objects.all().order_by('-data_inicio')
    return render(request, 'home.html', {
        'sintomas': sintomas,
        'tratamentos': tratamentos,
    })

def sintomas_list(request):
    sintomas = Sintoma.objects.all()
    return render(request, 'sintomas_list.html', {'sintomas': sintomas})

def sintoma_create(request):
    if request.method == 'POST':
        form = SintomaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sintomas_list')
    else:
        form = SintomaForm()
    return render(request, 'sintoma_form.html', {'form': form})

def sintoma_edit(request, pk):
    sintoma = get_object_or_404(Sintoma, pk=pk)
    if request.method == 'POST':
        form = SintomaForm(request.POST, instance=sintoma)
        if form.is_valid():
            form.save()
            return redirect('sintomas_list')
    else:
        form = SintomaForm(instance=sintoma)
    return render(request, 'sintoma_form.html', {'form': form})

def sintoma_delete(request, pk):
    sintoma = get_object_or_404(Sintoma, pk=pk)
    if request.method == 'POST':
        sintoma.delete()
        return redirect('sintomas_list')
    return render(request, 'sintoma_confirm_delete.html', {'sintoma': sintoma})

def tratamentos_list(request):
    tratamentos = Tratamento.objects.all()
    return render(request, 'tratamentos_list.html', {'tratamentos': tratamentos})

def tratamento_create(request):
    if request.method == 'POST':
        form = TratamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tratamentos_list')
    else:
        form = TratamentoForm()
    return render(request, 'tratamento_form.html', {'form': form})

def tratamento_edit(request, pk):
    tratamento = get_object_or_404(Tratamento, pk=pk)
    if request.method == 'POST':
        form = TratamentoForm(request.POST, instance=tratamento)
        if form.is_valid():
            form.save()
            return redirect('tratamentos_list')
    else:
        form = TratamentoForm(instance=tratamento)
    return render(request, 'tratamento_form.html', {'form': form})

def tratamento_delete(request, pk):
    tratamento = get_object_or_404(Tratamento, pk=pk)
    if request.method == 'POST':
        tratamento.delete()
        return redirect('tratamentos_list')
    return render(request, 'tratamento_confirm_delete.html', {'tratamento': tratamento})