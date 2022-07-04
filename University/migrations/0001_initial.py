# Generated by Django 4.0.6 on 2022-07-04 12:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('teacher', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('grade', models.IntegerField(validators=[django.core.validators.MaxValueValidator(20),
                                                          django.core.validators.MinValueValidator(0)])),
                ('cls',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='University.class')),
            ],
        ),
    ]