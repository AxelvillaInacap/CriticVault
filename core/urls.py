from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reviews.views import ReviewViewSet
from django.views.generic import TemplateView

# 1. Creamos el Router
router = DefaultRouter()

# 2. Registramos nuestra ruta "reviews"
# Esto generará urls como: /reviews/, /reviews/{id}/, etc.
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 3. Incluimos las rutas del router bajo el prefijo "api/v1/"
    # Versionar la API (v1) es una práctica de arquitectura esencial.
    path('api/v1/', include(router.urls)),

    path('', TemplateView.as_view(template_name='index.html')),
]