# Generated by Django 5.0.2 on 2024-03-06 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0013_alter_publications_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publications',
            name='likes',
            field=models.TextField(blank=True),
        ),
    ]
