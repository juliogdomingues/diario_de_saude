from django.urls import reverse, resolve

def test_urls_resolves():
    # Testa se as principais URLs resolvem para algum view
    assert resolve(reverse("home"))
    assert resolve(reverse("sintomas_list"))
    assert resolve(reverse("sintoma_create"))
    assert resolve(reverse("tratamentos_list"))
    assert resolve(reverse("tratamento_create"))

def test_urls_with_args():
    # Testa URLs que precisam de argumentos (pk)
    assert resolve(reverse("sintoma_edit", args=[1]))
    assert resolve(reverse("sintoma_delete", args=[1]))
    assert resolve(reverse("tratamento_edit", args=[1]))
    assert resolve(reverse("tratamento_delete", args=[1]))

def test_url_home_path():
    # Testa se a URL da home está correta
    url = reverse("home")
    assert url == "/"

def test_url_sintomas_list_path():
    # Testa se a URL da lista de sintomas contém a palavra 'sintoma'
    url = reverse("sintomas_list")
    assert "sintoma" in url

def test_url_tratamentos_list_path():
    # Testa se a URL da lista de tratamentos contém a palavra 'tratamento'
    url = reverse("tratamentos_list")
    assert "tratamento" in url