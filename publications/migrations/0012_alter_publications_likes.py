# Generated by Django 5.0.2 on 2024-03-04 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0011_alter_publications_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publications',
            name='likes',
            field=models.TextField(blank=True, default=0),
        ),
    ]
