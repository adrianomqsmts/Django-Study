from django.shortcuts import render
from .models import Produto
# Create your views here.

def index(request):
  #Dados do Models
  produtos = Produto.objects.all()
  context = {
    'produtos' : produtos
  }
  return render(request, 'index.html', context)