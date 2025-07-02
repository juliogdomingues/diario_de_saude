import pytest
from django.urls import reverse
from diario.models import Sintoma, Tratamento
from django.utils import timezone

@pytest.mark.django_db
def test_home_view_status_code(client):
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_home_view_contem_titulo(client):
    url = reverse("home")
    response = client.get(url)
    assert "Diário de Saúde" in response.content.decode()

@pytest.mark.django_db
def test_sintoma_edit_view(client):
    sintoma = Sintoma.objects.create(
        nome="Dor", descricao="Forte", data=timezone.now().date(), horario=timezone.now().time()
    )
    url = reverse("sintoma_edit", args=[sintoma.pk])
    response = client.get(url)
    assert response.status_code == 200
    data = {
        "nome": "Dor Editada",
        "descricao": "Editada",
        "data": sintoma.data.strftime("%Y-%m-%d"),
        "horario": sintoma.horario.strftime("%H:%M"),
    }
    response = client.post(url, data)
    assert response.status_code == 302
    sintoma.refresh_from_db()
    assert sintoma.nome == "Dor Editada"

@pytest.mark.django_db
def test_sintoma_delete_view(client):
    sintoma = Sintoma.objects.create(
        nome="Excluir", descricao="Teste", data=timezone.now().date(), horario=timezone.now().time()
    )
    url = reverse("sintoma_delete", args=[sintoma.pk])
    response = client.get(url)
    assert response.status_code == 200
    response = client.post(url)
    assert response.status_code == 302
    assert not Sintoma.objects.filter(pk=sintoma.pk).exists()

@pytest.mark.django_db
def test_tratamento_edit_view(client):
    tratamento = Tratamento.objects.create(
        nome="Tratamento", descricao="Desc", data_inicio=timezone.now().date(), data_fim=timezone.now().date()
    )
    url = reverse("tratamento_edit", args=[tratamento.pk])
    response = client.get(url)
    assert response.status_code == 200
    data = {
        "nome": "Tratamento Editado",
        "descricao": "Editado",
        "data_inicio": tratamento.data_inicio.strftime("%Y-%m-%d"),
        "data_fim": tratamento.data_fim.strftime("%Y-%m-%d"),
    }
    response = client.post(url, data)
    assert response.status_code == 302
    tratamento.refresh_from_db()
    assert tratamento.nome == "Tratamento Editado"

@pytest.mark.django_db
def test_tratamento_delete_view(client):
    tratamento = Tratamento.objects.create(
        nome="Excluir", descricao="Teste", data_inicio=timezone.now().date(), data_fim=timezone.now().date()
    )
    url = reverse("tratamento_delete", args=[tratamento.pk])
    response = client.get(url)
    assert response.status_code == 200
    response = client.post(url)
    assert response.status_code == 302
    assert not Tratamento.objects.filter(pk=tratamento.pk).exists()

@pytest.mark.django_db
def test_sintomas_list_view_status_code(client):
    url = reverse("sintomas_list")
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_tratamentos_list_view_status_code(client):
    url = reverse("tratamentos_list")
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_sintoma_create_view_get(client):
    url = reverse("sintoma_create")
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_tratamento_create_view_get(client):
    url = reverse("tratamento_create")
    response = client.get(url)
    assert response.status_code == 200