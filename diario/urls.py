from django.urls import path
from . import views

urlpatterns = [
    path('sintomas/', views.listar_sintomas, name='listar_sintomas'),
    path('sintomas/novo/', views.novo_sintoma, name='novo_sintoma'),
    path('tratamentos/', views.listar_tratamentos, name='listar_tratamentos'),
    path('tratamentos/novo/', views.novo_tratamento, name='novo_tratamento'),
]