# Generated by Django 5.0.2 on 2024-11-10 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0018_alter_publications_foto_alter_publications_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publications',
            name='foto',
            field=models.ImageField(blank=True, upload_to='imagenes'),
        ),
        migrations.AlterField(
            model_name='publications',
            name='pdf',
            field=models.FileField(blank=True, upload_to='imagenes'),
        ),
    ]
