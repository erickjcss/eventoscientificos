# Generated by Django 5.0.2 on 2024-03-02 00:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_alter_publications_foto_alter_publications_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publications',
            name='foto',
            field=models.CharField(blank=True, default='', max_length=100, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(100)]),
        ),
        migrations.AlterField(
            model_name='publications',
            name='pdf',
            field=models.CharField(blank=True, default='', max_length=100, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(100)]),
        ),
    ]
