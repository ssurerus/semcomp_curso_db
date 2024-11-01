from django.urls import path
from . import views

urlpatterns = [
    path('', views.inscricao_list, name='inscricao_list'),
    path('nova/', views.inscricao_create, name='inscricao_create'),
    path('editar/<int:id>/', views.inscricao_update, name='inscricao_update'),
    path('deletar/<int:id>/', views.inscricao_delete, name='inscricao_delete'),
    # Rotas para cursos semelhantes


    # Rotas de Cursos
    path('cursos/', views.curso_list, name='curso_list'),
    path('cursos/novo/', views.curso_create, name='curso_create'),
    path('cursos/<int:id>/editar/', views.curso_update, name='curso_update'),
    path('cursos/<int:id>/deletar/', views.curso_delete, name='curso_delete'),
]
