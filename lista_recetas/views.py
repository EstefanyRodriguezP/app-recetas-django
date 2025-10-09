from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Receta, MensajeContacto
from django.contrib import messages


# Create your views here.
def index(request):
    recetas = Receta.objects.all()
    return render(request, 'index.html', {'recetas': recetas})  

def recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'recetas.html', {'recetas': recetas})  

def receta_detalle(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    return render(request, 'recetas.html', {'receta': receta})

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')

        if not nombre or not email or not mensaje:
            messages.warning(request, 'Por favor, completa todos los campos.')
            return redirect('contacto')

        # Para guardar el mensaje en la base de datos
        MensajeContacto.objects.create(
            nombre=nombre,
            email=email,
            mensaje=mensaje
        )

        messages.success(request, '¡Gracias por tu mensaje! Te contactaremos pronto.')
        return redirect('mensaje_enviado')

    return render(request, 'contacto.html')

def mensaje_enviado(request):
    return render(request, 'mensaje_enviado.html')