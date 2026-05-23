from django.db import models

class Contratacion(models.Model):
    nombre_contacto = models.CharField(max_length=200, verbose_name="Nombre del Solicitante")
    empresa_marca = models.CharField(max_length=200, blank=True, null=True, verbose_name="Empresa o Marca")
    correo = models.EmailField(verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=50, blank=True, null=True, verbose_name="Teléfono de Contacto")
    mensaje = models.TextField(verbose_name="Propuesta o Detalles del Evento")
    fecha_envio = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Envío")

    class Meta:
        verbose_name = "Contratación"
        verbose_name_plural = "Contrataciones"
        ordering = ['-fecha_envio']

    def __str__(self):
        return f"Propuesta de {self.nombre_contacto} - {self.empresa_marca or 'Particular'}"

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
    
class Galeria(models.Model):
    TIPO_CHOICES = [
        ('foto', 'Foto'),
        ('video', 'Video'),
    ]
    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='foto')
    imagen = models.ImageField(upload_to='galeria/', blank=True, null=True)
    url_video = models.URLField(blank=True, null=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_subida']

    def __str__(self):
        return f"{self.titulo} ({self.get_tipo_display()})"