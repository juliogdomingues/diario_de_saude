import pytest
from diario.models import Sintoma, Tratamento
from django.utils import timezone

@pytest.mark.django_db
def test_criar_sintoma():
    sintoma = Sintoma.objects.create(
        nome="Dor de cabeça",
        descricao="Dor leve",
        data=timezone.now().date(),
        horario=timezone.now().time()
    )
    assert str(sintoma).startswith("Dor de cabeça")

@pytest.mark.django_db
def test_criar_tratamento():
    tratamento = Tratamento.objects.create(
        nome="Repouso",
        descricao="Descansar",
        data_inicio=timezone.now().date(),
        data_fim=timezone.now().date()
    )
    assert str(tratamento) == "Repouso"

@pytest.mark.django_db
def test_sintoma_str_retorna_nome_data_horario():
    sintoma = Sintoma.objects.create(
        nome="Febre",
        descricao="Alta",
        data=timezone.now().date(),
        horario=timezone.now().time()
    )
    s = str(sintoma)
    assert "Febre" in s and str(sintoma.data) in s and str(sintoma.horario)[:5] in s

@pytest.mark.django_db
def test_tratamento_str_retorna_nome():
    tratamento = Tratamento.objects.create(
        nome="Antibiótico",
        descricao="Uso oral",
        data_inicio=timezone.now().date(),
        data_fim=timezone.now().date()
    )
    assert str(tratamento) == "Antibiótico"

@pytest.mark.django_db
def test_sintoma_campos_obrigatorios():
    with pytest.raises(Exception):
        Sintoma.objects.create()

@pytest.mark.django_db
def test_tratamento_campos_obrigatorios():
    with pytest.raises(Exception):
        Tratamento.objects.create()