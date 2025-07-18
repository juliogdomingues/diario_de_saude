from django import forms
from .models import Sintoma, Tratamento
from django.utils import timezone

class SintomaForm(forms.ModelForm):
    class Meta:
        model = Sintoma
        fields = ['nome', 'descricao', 'data', 'horario']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'horario': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:
            now = timezone.localtime()
            self.fields['data'].initial = now.strftime('%Y-%m-%d')
            self.fields['horario'].initial = now.strftime('%H:%M')

class TratamentoForm(forms.ModelForm):
    class Meta:
        model = Tratamento
        fields = ['nome', 'descricao', 'data_inicio', 'data_fim']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:
            now = timezone.localtime()
            self.fields['data_inicio'].initial = now.strftime('%Y-%m-%d')

    def clean(self):
        cleaned_data = super().clean()
        data_inicio = cleaned_data.get("data_inicio")
        data_fim = cleaned_data.get("data_fim")
        if data_inicio and data_fim and data_fim < data_inicio:
            self.add_error("data_fim", "A data final não pode ser anterior à data inicial.")