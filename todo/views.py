from django.shortcuts import render

# Create your views here.
#from django.shortcuts import render
from .models import Tarefa

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'todo/lista_tarefas.html', {'tarefas': tarefas})


