from diario.forms import SintomaForm, TratamentoForm

def test_sintoma_form_valido():
    data = {
        "nome": "Tosse",
        "descricao": "Tosse seca",
        "data": "2024-06-01",
        "horario": "10:00"
    }
    form = SintomaForm(data=data)
    assert form.is_valid()

def test_sintoma_form_invalido():
    data = {
        "nome": "",
        "descricao": "Sem nome",
        "data": "2024-06-01",
        "horario": "10:00"
    }
    form = SintomaForm(data=data)
    assert not form.is_valid()
    assert "nome" in form.errors

def test_tratamento_form_valido():
    data = {
        "nome": "Fisioterapia",
        "descricao": "Sessões semanais",
        "data_inicio": "2024-06-01",
        "data_fim": "2024-06-10"
    }
    form = TratamentoForm(data=data)
    assert form.is_valid()

def test_tratamento_form_invalido():
    data = {
        "nome": "",
        "descricao": "Sem nome",
        "data_inicio": "2024-06-01",
        "data_fim": "2024-06-10"
    }
    form = TratamentoForm(data=data)
    assert not form.is_valid()
    assert "nome" in form.errors