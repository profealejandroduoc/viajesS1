from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'tourapp/index.html')

def paquetes(request):
    return render(request,'tourapp/paquetes.html')

def productos(request):
    return render(request,'tourapp/productos.html')