from django.shortcuts import render
from .models import Activo

def activos_view(request):
    activos = Activo.objects.all()
    return render(request, 'app_activos/activos.html', {'activos': activos})
