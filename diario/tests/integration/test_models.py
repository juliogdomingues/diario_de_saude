import pytest
from django.urls import reverse
from django.utils import timezone
from diario.models import Sintoma, Tratamento

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


# testes CRUD para sintoma, um para cada.
@pytest.mark.django_db
def test_create_sintoma(client):
    url = reverse('sintoma_create')
    data = {
        "nome": "Tosse",
        "descricao": "Tosse persistente",
        "data": timezone.now().date().strftime('%Y-%m-%d'),
        "horario": timezone.now().time().strftime('%H:%M'),
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Sintoma.objects.filter(nome="Tosse").exists()

@pytest.mark.django_db
def test_retrieve_sintoma(client):
    sintoma = Sintoma.objects.create(nome="Tosse", descricao="Persistente", data=timezone.now().date(), horario=timezone.now().time())
    response = client.get(reverse('sintomas_list'))
    assert "Tosse" in response.content.decode()

@pytest.mark.django_db
def test_update_sintoma(client):
    sintoma = Sintoma.objects.create(nome="Tosse", descricao="Persistente", data=timezone.now().date(), horario=timezone.now().time())
    update_url = reverse('sintoma_edit', args=[sintoma.pk])
    new_data = {
        "nome": "Tosse Severa",
        "descricao": "Muito Persistente",
        "data": sintoma.data.strftime("%Y-%m-%d"),
        "horario": sintoma.horario.strftime("%H:%M"),
    }
    response = client.post(update_url, new_data)
    assert response.status_code == 302
    sintoma.refresh_from_db()
    assert sintoma.nome == "Tosse Severa"

@pytest.mark.django_db
def test_delete_sintoma(client):
    sintoma = Sintoma.objects.create(nome="Tosse", descricao="Persistente", data=timezone.now().date(), horario=timezone.now().time())
    delete_url = reverse('sintoma_delete', args=[sintoma.pk])
    response = client.post(delete_url)
    assert response.status_code == 302
    assert not Sintoma.objects.filter(id=sintoma.id).exists()


#testes CRUD para tratamento, um para cada

@pytest.mark.django_db
def test_create_tratamento(client):
    create_url = reverse('tratamento_create')
    data = {
        "nome": "Fisioterapia",
        "descricao": "Sessões semanais",
        "data_inicio": timezone.now().date().strftime('%Y-%m-%d'),
        "data_fim": (timezone.now().date() + timezone.timedelta(days=10)).strftime('%Y-%m-%d'),
    }
    response = client.post(create_url, data)
    assert response.status_code == 302
    assert Tratamento.objects.filter(nome="Fisioterapia").exists()

@pytest.mark.django_db
def test_retrieve_tratamento(client):
    tratamento = Tratamento.objects.create(
        nome="Fisioterapia",
        descricao="Sessões semanais",
        data_inicio=timezone.now().date(),
        data_fim=timezone.now().date() + timezone.timedelta(days=10)
    )
    response = client.get(reverse('tratamentos_list'))
    assert response.status_code == 200
    assert "Fisioterapia" in response.content.decode()

@pytest.mark.django_db
def test_update_tratamento(client):
    tratamento = Tratamento.objects.create(
        nome="Fisioterapia",
        descricao="Sessões semanais",
        data_inicio=timezone.now().date(),
        data_fim=timezone.now().date() + timezone.timedelta(days=10)
    )
    update_url = reverse('tratamento_edit', args=[tratamento.pk])
    new_data = {
        "nome": "Fisioterapia Intensiva",
        "descricao": "Sessões intensivas",
        "data_inicio": tratamento.data_inicio.strftime('%Y-%m-%d'),
        "data_fim": tratamento.data_fim.strftime('%Y-%m-%d'),
    }
    response = client.post(update_url, new_data)
    assert response.status_code == 302
    tratamento.refresh_from_db()
    assert tratamento.nome == "Fisioterapia Intensiva"

@pytest.mark.django_db
def test_delete_tratamento(client):
    tratamento = Tratamento.objects.create(
        nome="Fisioterapia",
        descricao="Sessões semanais",
        data_inicio=timezone.now().date(),
        data_fim=timezone.now().date() + timezone.timedelta(days=10)
    )
    delete_url = reverse('tratamento_delete', args=[tratamento.pk])
    response = client.post(delete_url)
    assert response.status_code == 302
    assert not Tratamento.objects.filter(id=tratamento.pk).exists()

@pytest.mark.django_db
def test_sintomas_repetidos(client):
    url = reverse('sintoma_create')
    data = {
        "nome": "Tosse",
        "descricao": "Leve",
        "data": timezone.now().date().strftime('%Y-%m-%d'),
        "horario": timezone.now().time().strftime('%H:%M'),
    }
    response1 = client.post(url, data)
    response2 = client.post(url, data)
    assert response1.status_code == 302
    assert response2.status_code == 302
    assert Sintoma.objects.filter(nome="Tosse").count() == 2
