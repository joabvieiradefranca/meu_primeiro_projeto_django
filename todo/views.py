'''from django.shortcuts import render

# Create your views here.
#from django.shortcuts import render
from .models import Tarefa

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'todo/lista_tarefas.html', {'tarefas': tarefas})

from django.shortcuts import render, redirect
from .models import Tarefa

def lista_tarefas(request):
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        if descricao:
            Tarefa.objects.create(descricao=descricao, concluida=False)
            return redirect('lista_tarefas')  # Evita reenvio do formulário
    tarefas = Tarefa.objects.all()
    return render(request, 'todo/lista_tarefas.html', {'tarefas': tarefas})'''


from django.shortcuts import render, redirect
from .models import Tarefa

def lista_tarefas(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        if titulo:
            Tarefa.objects.create(titulo=titulo, descricao=descricao)
        return redirect('lista_tarefas')  # Redireciona após o envio

    tarefas = Tarefa.objects.all()
    return render(request, 'todo/lista_tarefas.html', {'tarefas': tarefas})

from django.shortcuts import get_object_or_404

def concluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.concluida = True
    tarefa.save()
    return redirect('lista_tarefas')

def excluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()
    return redirect('lista_tarefas')

