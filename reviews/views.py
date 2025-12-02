from rest_framework import viewsets
from .models import Review
from .serializers import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    # Queryset: ¿Qué datos voy a buscar a la base de datos?
    queryset = Review.objects.all()
    # Serializer: ¿Cómo convierto esos datos a JSON?
    serializer_class = ReviewSerializer