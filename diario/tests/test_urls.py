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