# Generated by Django 5.0.2 on 2024-03-06 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0004_personas_equivocaciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='personas',
            name='uso',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
