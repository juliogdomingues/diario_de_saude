from django.shortcuts import render, redirect
from .models import Sintoma, Tratamento
from .forms import SintomaForm, TratamentoForm
from django.contrib.auth.decorators import login_required

@login_required
def listar_sintomas(request):
    sintomas = Sintoma.objects.filter(usuario=request.user)
    return render(request, 'diario/sintomas_list.html', {'sintomas': sintomas})

@login_required
def novo_sintoma(request):
    if request.method == 'POST':
        form = SintomaForm(request.POST)
        if form.is_valid():
            sintoma = form.save(commit=False)
            sintoma.usuario = request.user
            sintoma.save()
            return redirect('listar_sintomas')
    else:
        form = SintomaForm()
    return render(request, 'diario/sintoma_form.html', {'form': form})

@login_required
def listar_tratamentos(request):
    tratamentos = Tratamento.objects.filter(usuario=request.user)
    return render(request, 'diario/tratamentos_list.html', {'tratamentos': tratamentos})

@login_required
def novo_tratamento(request):
    if request.method == 'POST':
        form = TratamentoForm(request.POST)
        if form.is_valid():
            tratamento = form.save(commit=False)
            tratamento.usuario = request.user
            tratamento.save()
            return redirect('listar_tratamentos')
    else:
        form = TratamentoForm()
    return render(request, 'diario/tratamento_form.html', {'form': form})