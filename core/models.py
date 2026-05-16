from django.db import models

# REVISA ESTA CLASE: Asegúrate de que se llame exactamente Concierto
class Concierto(models.Model):
    ciudad = models.CharField(max_length=100)
    lugar = models.CharField(max_length=200)
    fecha = models.DateTimeField()
    link_tickets = models.URLField(blank=True)

    def __str__(self):
        return f"{self.ciudad} - {self.fecha.strftime('%d/%m/%Y')}"

class Album(models.Model):
    TIPO_CHOICES = [
        ('SINGLE', 'Single / EP'),
        ('ALBUM', 'Álbum de Estudio'),
    ]
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='ALBUM')
    fecha_lanzamiento = models.DateField()
    portada = models.ImageField(upload_to='discografia/')
    link_streaming = models.URLField(blank=True, help_text="Link a Spotify / Apple Music")

    def __str__(self):
        return f"{self.titulo} ({self.get_tipo_display()})"

class Cancion(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='canciones')
    titulo = models.CharField(max_length=200)
    duracion = models.CharField(max_length=10, help_text="Ejemplo: 3:15")
    numero_pista = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['numero_pista']

    def __str__(self):
        return f"{self.numero_pista}. {self.titulo}"

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='merch/')
    descripcion = models.TextField(blank=True, verbose_name="Descripción del producto")
    stock = models.IntegerField(default=0)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

class Biografia(models.Model):
    texto_principal = models.TextField()
    imagen_perfil = models.ImageField(upload_to='about/')
    link_instagram = models.URLField(blank=True)
    link_youtube = models.URLField(blank=True)

    class Meta:
        verbose_name = "Biografía"
        verbose_name_plural = "Biografía"

    def __str__(self):
        return "Biografía de Alan Wittels"