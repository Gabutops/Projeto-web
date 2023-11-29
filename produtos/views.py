from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import *

def index(request):
    ultimos_produtos_adicionados = Produtos.objects.all()
    template = loader.get_template("produtos/home.html")
    context = {
        'produtos': ultimos_produtos_adicionados
    }
    return render(request=request,template_name='produtos/home.html',context= context)