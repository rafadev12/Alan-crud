from django.shortcuts import render, redirect
from .models import Biografia, Album, Concierto, Producto, Galeria, Contratacion

def home(request):
    # Procesar formulario de contratación si viene por POST
    msg_exito = False
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        empresa = request.POST.get('empresa')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        mensaje = request.POST.get('mensaje')
        
        # Validamos que los campos obligatorios traigan algo
        if nombre and correo and mensaje:
            Contratacion.objects.create(
                nombre_contacto=nombre,
                empresa_marca=empresa,
                correo=correo,
                telefono=telefono,
                mensaje=mensaje
            )
            msg_exito = True # Activamos bandera de éxito para el HTML

    biografia = Biografia.objects.first()
    albumes = Album.objects.all()
    productos = Producto.objects.all()
    conciertos = Concierto.objects.all().order_by('fecha')
    items_galeria = Galeria.objects.all()[:6]
    
    context = {
        'biografia': biografia,
        'albumes': albumes,
        'productos': productos,
        'conciertos': conciertos,
        'items_galeria': items_galeria,
        'msg_exito': msg_exito, # <-- Lo pasamos al contexto
    }
    return render(request, 'core/home.html', context)

def tours(request):
    conciertos = Concierto.objects.all().order_by('fecha')
    return render(request, 'core/tours.html', {'conciertos': conciertos})

def discografia(request):
    albumes = Album.objects.all().order_by('-fecha_lanzamiento') 
    return render(request, 'core/discografia.html', {'albumes': albumes})

def galeria(request):
    items = Galeria.objects.all()
    return render(request, 'core/galeria.html', {'items': items})