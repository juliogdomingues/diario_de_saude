import pytest
from diario.models import Sintoma, Tratamento
from django.utils import timezone

@pytest.mark.django_db
def test_criar_sintoma():
    sintoma = Sintoma.objects.create(nome="Dor de cabeça", descricao="Dor leve")
    assert sintoma.nome == "Dor de cabeça"

@pytest.mark.django_db
def test_criar_tratamento():
    sintoma = Sintoma.objects.create(nome="Febre", descricao="Alta")
    tratamento = Tratamento.objects.create(
        nome="Paracetamol",
        descricao="Tomar 3x ao dia",
        data_inicio=timezone.now().date()
    )
    tratamento.sintomas.add(sintoma)
    assert tratamento.sintomas.count() == 1