import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Student, Class


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'name', 'teacher']
        read_only_fields = ('id',)


class StudentSerializer(serializers.ModelSerializer):
    EMAIL_REGEX = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    class_data = ClassSerializer(source='class_id', read_only=True)

    def validate_email(self, email):
        if not re.fullmatch(self.EMAIL_REGEX, email):
            raise ValidationError("email is not valid")
        return email

    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'class_data', 'class_id', 'score']
        read_only_fields = ('id',)
        extra_kwargs = {
            'class_id': {
                'write_only': True
            }
        }
