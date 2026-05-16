from django.contrib import admin
# CAMBIA 'Conciertos' por 'Concierto' en la línea de abajo:
from .models import Concierto, Album, Cancion, Producto, Biografia

# 1. Configuración para los Conciertos
@admin.register(Concierto) # Asegúrate de que aquí también esté en singular
class ConciertoAdmin(admin.ModelAdmin):
    list_display = ('ciudad', 'lugar', 'fecha', 'link_tickets')
    list_filter = ('fecha', 'ciudad')
    search_fields = ('ciudad', 'lugar')

# 2. Configuración inline para Canciones (Permite añadir canciones directamente dentro del Álbum)
class CancionInline(admin.TabularInline):
    model = Cancion
    extra = 3 # Te muestra 3 espacios vacíos por defecto para añadir temas rápidamente

# 3. Configuración para los Álbumes
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'fecha_lanzamiento')
    list_filter = ('tipo', 'fecha_lanzamiento')
    search_fields = ('titulo',)
    inlines = [CancionInline] # Metemos las canciones aquí dentro

# 4. Configuración para la Tienda (Merch)
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'disponible')
    list_editable = ('precio', 'stock', 'disponible') # Permite editar directo desde la lista sin entrar al producto
    list_filter = ('disponible',)
    search_fields = ('nombre',)

# 5. Configuración para la Biografía
@admin.register(Biografia)
class BiografiaAdmin(admin.ModelAdmin):
    # Al ser solo una biografía, limitamos para que no llenen la lista de registros innecesarios
    def has_add_permission(self, request):
        # Si ya existe una biografía creada, no permite crear otra, solo editar la existente
        if Biografia.objects.exists():
            return False
        return True