from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sintomas/', views.sintomas_list, name='sintomas_list'),
    path('sintomas/novo/', views.sintoma_create, name='sintoma_create'),
    path('sintomas/<int:pk>/editar/', views.sintoma_edit, name='sintoma_edit'),
    path('sintomas/<int:pk>/remover/', views.sintoma_delete, name='sintoma_delete'),
    path('tratamentos/', views.tratamentos_list, name='tratamentos_list'),
    path('tratamentos/novo/', views.tratamento_create, name='tratamento_create'),
    path('tratamentos/<int:pk>/editar/', views.tratamento_edit, name='tratamento_edit'),
    path('tratamentos/<int:pk>/remover/', views.tratamento_delete, name='tratamento_delete'),
]