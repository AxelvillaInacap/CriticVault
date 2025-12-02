import uuid
from django.db import models

class Review(models.Model):
    # Definimos las categorías como constantes
    CATEGORIES = [
        ('TECH', 'Tecnología'),
        ('GAME', 'Videojuegos'),
        ('MOVIE', 'Cine y Series'),
        ('AUDIO', 'Audiófilo'),
    ]

    # ID profesional: UUID no secuencial
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    title = models.CharField(max_length=255, verbose_name="Título")
    category = models.CharField(max_length=10, choices=CATEGORIES, default='TECH')
    
    # Rating: Usamos PositiveSmallIntegerField para ahorrar espacio
    rating = models.PositiveSmallIntegerField(help_text="Puntuación del 1 al 10")
    
    content = models.TextField(verbose_name="Opinión")
    
    # Timestamps automáticos (Clave para ordenar y auditar)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at'] # Ordenar por defecto: lo más nuevo primero
        verbose_name = "Reseña"
        verbose_name_plural = "Reseñas"

    def __str__(self):
        return f"{self.title} ({self.rating}/10)"