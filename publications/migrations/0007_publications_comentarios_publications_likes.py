# Generated by Django 5.0.2 on 2024-03-02 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0006_alter_publications_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='publications',
            name='comentarios',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='publications',
            name='likes',
            field=models.ImageField(blank=True, default=0, upload_to=''),
        ),
    ]
