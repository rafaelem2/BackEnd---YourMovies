from rest_framework import serializers
from .models import Favorite


class favoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['title']