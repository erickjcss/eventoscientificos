# Generated by Django 5.0.2 on 2024-03-02 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0007_publications_comentarios_publications_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publications',
            name='likes',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
