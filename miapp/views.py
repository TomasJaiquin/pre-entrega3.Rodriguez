from django.shortcuts import render

# crear vistas aca.

from django.shortcuts import render
from .forms import CategoriaForm, ProductoForm, ClienteForm
from .models import Categoria, Producto, Cliente

def index(request):
    return render(request, 'miapp/index.html')

# Otras vistas aca

def buscar(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        resultados = Producto.objects.filter(nombre__icontains=query)
    else:
        resultados = None
    return render(request, 'miapp/buscar.html', {'resultados': resultados})

from django.shortcuts import render

def index(request):
    return render(request, 'miapp/index.html')

from django.shortcuts import render

def buscar(request):
    if 'q' in request.GET:
        query = request.GET['q']
        
        resultados = []  
    else:
        resultados = None

    return render(request, 'miapp/buscar.html', {'resultados': resultados})

# Otras vistas aca

from django.shortcuts import render

def main(request):
    return render(request, 'miapp/main.html')

