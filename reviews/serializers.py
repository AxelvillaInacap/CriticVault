from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        # Importante: Estos campos no deben ser editables por el usuario
        read_only_fields = ('id', 'created_at', 'updated_at')

    # Validación personalizada
    def validate_rating(self, value):
        if value < 1 or value > 10:
            raise serializers.ValidationError("La puntuación debe estar entre 1 y 10.")
        return value