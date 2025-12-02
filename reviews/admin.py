from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # ¿Qué columnas mostrar en la lista?
    list_display = ('title', 'category', 'rating', 'created_at')
    
    # ¿Por qué campos puedo filtrar a la derecha?
    list_filter = ('category', 'rating', 'created_at')
    
    # ¿Por qué campos puedo buscar?
    search_fields = ('title', 'content')
    
    # ¿Cómo ordenar por defecto?
    ordering = ('-created_at',)
    
    # Solo lectura para campos sensibles (para que no los edites por error)
    readonly_fields = ('id', 'created_at', 'updated_at')