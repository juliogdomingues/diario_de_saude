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