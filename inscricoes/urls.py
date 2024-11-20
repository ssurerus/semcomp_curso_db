from django.urls import path
from . import views

urlpatterns = [
    #Define os "caminhos"/Url's das páginas de manipulação da tabela Incricao

    #Listagem de inscrições, referente a query SELECT * FROM Inscricao (SQL puro)
    path('', views.inscricao_list, name='inscricao_list'),

    #Criação de inscrições, referente a query INSERT INTO Inscricao (SQL puro)
    path('nova/', views.inscricao_create, name='inscricao_create'),

    #Edição de inscrições, referente a query UPDATE Inscricao (SQL puro)
    path('editar/<int:id>/', views.inscricao_update, name='inscricao_update'),

    #Deleção de inscrições, referente a query DELETE FROM Inscricao (SQL puro)
    path('deletar/<int:id>/', views.inscricao_delete, name='inscricao_delete'),
    


    #Define os "caminhos"/Url's das páginas de manipulação da tabela Curso

    #Listagem de cursos, referente a query SELECT * FROM Curso (SQL puro)
    path('cursos/', views.curso_list, name='curso_list'),

    #Criação de cursos, referente a query INSERT INTO Curso (SQL puro)
    path('cursos/novo/', views.curso_create, name='curso_create'),

    #Edição de cursos, referente a query UPDATE Curso (SQL puro)
    path('cursos/<int:id>/editar/', views.curso_update, name='curso_update'),

    #Deleção de cursos, referente a query DELETE FROM Curso (SQL puro)
    path('cursos/<int:id>/deletar/', views.curso_delete, name='curso_delete'),
]
