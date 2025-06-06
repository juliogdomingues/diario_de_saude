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

def test_sintoma_form_invalido_nome_vazio():
    data = {
        "nome": "",
        "descricao": "Sem nome",
        "data": "2024-06-01",
        "horario": "10:00"
    }
    form = SintomaForm(data=data)
    assert not form.is_valid()
    assert "nome" in form.errors

def test_sintoma_form_invalido_data_vazia():
    data = {
        "nome": "Dor",
        "descricao": "Teste",
        "data": "",
        "horario": "10:00"
    }
    form = SintomaForm(data=data)
    assert not form.is_valid()
    assert "data" in form.errors

def test_sintoma_form_invalido_horario_vazio():
    data = {
        "nome": "Dor",
        "descricao": "Teste",
        "data": "2024-06-01",
        "horario": ""
    }
    form = SintomaForm(data=data)
    assert not form.is_valid()
    assert "horario" in form.errors

def test_tratamento_form_valido():
    data = {
        "nome": "Fisioterapia",
        "descricao": "Sessões semanais",
        "data_inicio": "2024-06-01",
        "data_fim": "2024-06-10"
    }
    form = TratamentoForm(data=data)
    assert form.is_valid()

def test_tratamento_form_invalido_nome_vazio():
    data = {
        "nome": "",
        "descricao": "Sem nome",
        "data_inicio": "2024-06-01",
        "data_fim": "2024-06-10"
    }
    form = TratamentoForm(data=data)
    assert not form.is_valid()
    assert "nome" in form.errors

def test_tratamento_form_invalido_data_inicio_vazia():
    data = {
        "nome": "Tratamento",
        "descricao": "Teste",
        "data_inicio": "",
        "data_fim": "2024-06-10"
    }
    form = TratamentoForm(data=data)
    assert not form.is_valid()
    assert "data_inicio" in form.errors

def test_tratamento_form_invalido_data_fim_vazia():
    data = {
        "nome": "Tratamento",
        "descricao": "Teste",
        "data_inicio": "2024-06-01",
        "data_fim": ""
    }
    form = TratamentoForm(data=data)
    assert not form.is_valid()
    assert "data_fim" in form.errors

def test_tratamento_form_data_fim_antes_data_inicio():
    data = {
        "nome": "Tratamento",
        "descricao": "Teste",
        "data_inicio": "2024-06-10",
        "data_fim": "2024-06-01"
    }
    form = TratamentoForm(data=data)
    assert not form.is_valid()
    assert "data_fim" in form.errors

def test_sintoma_form_widget_data():
    form = SintomaForm()
    assert form.fields["data"].widget.input_type == "date"

def test_sintoma_form_widget_horario():
    form = SintomaForm()
    assert form.fields["horario"].widget.input_type == "time"

def test_tratamento_form_fields():
    form = TratamentoForm()
    assert set(form.fields.keys()) == {"nome", "descricao", "data_inicio", "data_fim"}