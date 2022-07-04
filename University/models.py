from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    teacher = models.CharField(max_length=100, null=False, blank=False)


class Student(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    cls = models.ForeignKey(to=Class, on_delete=models.deletion.SET_NULL, null=True)
    grade = models.IntegerField(validators=[MaxValueValidator(20), MinValueValidator(0)])
