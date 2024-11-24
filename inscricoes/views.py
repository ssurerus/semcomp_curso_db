from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from .forms import InscricaoForm, CursoForm
from .models import Inscricao, Curso

# Listagem de inscrições, nessa função temos uma query que selciona todos os campos da tabela Inscricao junto com o nome do curso que o aluno está inscrito (JOIN) e retorna para nossa página HTML;
#O JOIN é uma cláusula SQL que é usada para combinar linhas de duas ou mais tabelas, com base em um campo relacionado entre elas.
def inscricao_list(request):
    with connection.cursor() as cursor:

 ################################ DESAFIO ################################       

        #Query de seleção -> 

        #Descomente a linha abaixo
        cursor.execute("SUA QUERY AQUI")

        #Exclua a linha 20 e descomente a linha 19 para visualizar a listagem na página HTML
        # inscricoes = cursor.fetchall()
        inscricoes = []

################################ DESAFIO ################################


    return render(request, 'inscricoes/inscricao_list.html', {'inscricoes': inscricoes})

#Criação de inscrições, nessa função temos a seleção de todos os cursos inicialmente para que eles possam ser associados a uma inscrição, e caso o método seja POST, ou seja, o usuário tenha preenchido o formulário e clicado em enviar, os dados são inseridos na tabela Inscricao e o usuário é redirecionado para a página de listagem de inscrições.
def inscricao_create(request):
    cursos = []
    with connection.cursor() as cursor:
        #Query de seleção de cursos->
        cursor.execute("SELECT * FROM inscricoes_curso")
        cursos = cursor.fetchall()

    if request.method == 'POST':
        nome = request.POST['nome_completo']
        matricula = request.POST['matricula']
        email = request.POST['email']
        curso_id = request.POST['curso_id']

        with connection.cursor() as cursor:
            #Query de inserção de inscrição ->
            cursor.execute("INSERT INTO inscricoes_inscricao (nome_completo, matricula, email, curso_id) VALUES (%s, %s, %s, %s)", [nome, matricula, email, curso_id])
        return redirect('inscricao_list')
    
    return render(request, 'inscricoes/inscricao_form.html', {'cursos': cursos})

#Edição de inscrições, nessa função temos a seleção de todos os cursos inicialmente para que eles possam ser associados a uma inscrição, e caso o método seja POST, ou seja, o usuário tenha preenchido o formulário e clicado em enviar, os dados são atualizados na tabela Inscricao e o usuário é redirecionado para a página de listagem de inscrições.
def inscricao_update(request, id):
    cursos = []
    with connection.cursor() as cursor:
        #Query de seleção de cursos->
        cursor.execute("SELECT * FROM inscricoes_curso")
        cursos = cursor.fetchall()
    
    if request.method == 'POST':
        nome = request.POST['nome_completo']
        matricula = request.POST['matricula']
        email = request.POST['email']
        curso_id = request.POST['curso_id']

        with connection.cursor() as cursor:
            #Query de atualização de inscrição ->
            cursor.execute("UPDATE inscricoes_inscricao SET nome_completo = %s, matricula = %s, email = %s, curso_id = %s WHERE id = %s", [nome, matricula, email, curso_id, id])
        return redirect('inscricao_list')
    
    with connection.cursor() as cursor:
        #Query de seleção de inscrição ->
        cursor.execute("SELECT * FROM inscricoes_inscricao WHERE id = %s", [id])
        inscricao = cursor.fetchone()

    return render(request, 'inscricoes/inscricao_form.html', {'inscricao': inscricao, 'cursos': cursos})


#Deleção de inscrições, nessa função temos a deleção de uma inscrição com base no id passado como parâmetro, e caso o método seja POST, ou seja, o usuário tenha clicado em confirmar a deleção, a inscrição é deletada da tabela Inscricao e o usuário é redirecionado para a página de listagem de inscrições.
def inscricao_delete(request, id):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM inscricoes_inscricao WHERE id = %s", [id])
        return redirect('inscricao_list')
    
    return render(request, 'inscricoes/inscricao_delete.html', {'id': id})

# Similar as funções de inscrição, porém com a tabela Curso

def curso_list(request):
    with connection.cursor() as cursor:
        #Query de seleção ->
        cursor.execute("SELECT * FROM inscricoes_curso")
        cursos = cursor.fetchall()
    print(cursos)
    return render(request, 'inscricoes/curso_list.html', {'cursos': cursos})

def curso_create(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            descricao = form.cleaned_data['descricao']
            with connection.cursor() as cursor:
                #Query de inserção ->
                cursor.execute("INSERT INTO inscricoes_curso (nome, descricao) VALUES (%s, %s)", [nome, descricao])
            return redirect('curso_list')
    else:
        form = CursoForm()
    return render(request, 'inscricoes/curso_form.html', {'form': form})

def curso_update(request, id):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            descricao = form.cleaned_data['descricao']
            with connection.cursor() as cursor:
                #Query de atualização ->
                cursor.execute("UPDATE inscricoes_curso SET nome = %s, descricao = %s WHERE id = %s", [nome, descricao, id])
            return redirect('curso_list')
    else:
        with connection.cursor() as cursor:
            #Query de seleção ->
            cursor.execute("SELECT nome, descricao FROM inscricoes_curso WHERE id = %s", [id])
            curso = cursor.fetchone()
        form = CursoForm(initial={'nome': curso[0], 'descricao': curso[1]})
    return render(request, 'inscricoes/curso_form.html', {'form': form})

def curso_delete(request, id):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            #Query de deleção ->
            cursor.execute("DELETE FROM inscricoes_curso WHERE id = %s", [id])
        return redirect('curso_list')
    return render(request, 'inscricoes/curso_delete.html', {'id': id})