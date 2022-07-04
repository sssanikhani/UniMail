from rest_framework import serializers

from .models import Student, Class


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'name', 'teacher']
        read_only_fields = ('id',)
