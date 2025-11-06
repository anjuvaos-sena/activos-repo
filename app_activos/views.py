from django.shortcuts import redirect, render
from .models import Activo

def activos_view(request):
    activos = Activo.objects.all()
    return render(request, 'app_activos/activos.html', {'activos': activos})

def crear_activo_view(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        marca = request.POST.get('marca')
        estado = request.POST.get('estado')
        nuevo_activo = Activo(codigo=codigo, nombre=nombre, marca=marca, estado=estado)
        nuevo_activo.save()
        return redirect('activos')
    return render(request, 'app_activos/crear_activo.html')