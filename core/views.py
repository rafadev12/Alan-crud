from django.shortcuts import render
from .models import Biografia, Album, Concierto, Producto

def home(request):
    biografia = Biografia.objects.first()
    albumes = Album.objects.all()
    productos = Producto.objects.all()
    conciertos = Concierto.objects.all().order_by('fecha')
    
    context = {
        'biografia': biografia,
        'albumes': albumes,
        'productos': productos,
        'conciertos': conciertos,
    }
    
    return render(request, 'core/home.html', context)


def tours(request):
    conciertos = Concierto.objects.all().order_by('fecha')
    return render(request, 'core/tours.html', {'conciertos': conciertos})

def discografia(request):
    albumes = Album.objects.all().order_by('-fecha_lanzamiento') 
    return render(request, 'core/discografia.html', {'albumes': albumes})