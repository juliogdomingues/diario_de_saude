{% extends 'diario/base.html' %}
{% block content %}
<h2>Tratamentos</h2>
<ul>
    {% for tratamento in tratamentos %}
        <li>{{ tratamento.titulo }} - {{ tratamento.descricao }} - {{ tratamento.data }}</li>
    {% empty %}
        <li>Nenhum tratamento cadastrado.</li>
    {% endfor %}
</ul>
{% endblock %}