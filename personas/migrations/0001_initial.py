# Generated by Django 5.0.2 on 2024-02-29 23:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePer', models.CharField(max_length=20)),
                ('apellidos', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contr', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(100)])),
                ('esTrabajador', models.BooleanField(default=True)),
                ('catdoc', models.CharField(max_length=50)),
            ],
        ),
    ]
