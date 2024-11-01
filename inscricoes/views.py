from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from .forms import InscricaoForm, CursoForm
from .models import Inscricao, Curso

# Inscrição - CREATE (SQL puro)
def inscricao_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT i.id, i.nome_completo, i.matricula, i.email, c.nome FROM Inscricao i JOIN Curso c ON i.curso_id = c.id")
        inscricoes = cursor.fetchall()
    return render(request, 'inscricoes/inscricao_list.html', {'inscricoes': inscricoes})

def inscricao_create(request):
    cursos = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Curso")
        cursos = cursor.fetchall()

    if request.method == 'POST':
        nome = request.POST['nome_completo']
        matricula = request.POST['matricula']
        email = request.POST['email']
        curso_id = request.POST['curso_id']

        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO Inscricao (nome_completo, matricula, email, curso_id) VALUES (%s, %s, %s, %s)", [nome, matricula, email, curso_id])
        return redirect('inscricao_list')
    
    return render(request, 'inscricoes/inscricao_form.html', {'cursos': cursos})

def inscricao_update(request, id):
    cursos = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Curso")
        cursos = cursor.fetchall()
    
    if request.method == 'POST':
        nome = request.POST['nome_completo']
        matricula = request.POST['matricula']
        email = request.POST['email']
        curso_id = request.POST['curso_id']

        with connection.cursor() as cursor:
            cursor.execute("UPDATE Inscricao SET nome_completo = %s, matricula = %s, email = %s, curso_id = %s WHERE id = %s", [nome, matricula, email, curso_id, id])
        return redirect('inscricao_list')
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Inscricao WHERE id = %s", [id])
        inscricao = cursor.fetchone()

    return render(request, 'inscricoes/inscricao_form.html', {'inscricao': inscricao, 'cursos': cursos})

def inscricao_delete(request, id):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM Inscricao WHERE id = %s", [id])
        return redirect('inscricao_list')
    
    return render(request, 'inscricoes/inscricao_delete.html', {'id': id})

# Similar para CRUD de Cursos (CREATE, READ, UPDATE, DELETE)

def curso_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Curso")
        cursos = cursor.fetchall()
    return render(request, 'inscricoes/curso_list.html', {'cursos': cursos})

def curso_create(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            descricao = form.cleaned_data['descricao']
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO Curso (nome, descricao) VALUES (%s, %s)", [nome, descricao])
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
                cursor.execute("UPDATE Curso SET nome = %s, descricao = %s WHERE id = %s", [nome, descricao, id])
            return redirect('curso_list')
    else:
        with connection.cursor() as cursor:
            cursor.execute("SELECT nome, descricao FROM Curso WHERE id = %s", [id])
            curso = cursor.fetchone()
        form = CursoForm(initial={'nome': curso[0], 'descricao': curso[1]})
    return render(request, 'inscricoes/curso_form.html', {'form': form})

def curso_delete(request, id):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM Curso WHERE id = %s", [id])
        return redirect('curso_list')
    return render(request, 'inscricoes/curso_delete.html', {'id': id})