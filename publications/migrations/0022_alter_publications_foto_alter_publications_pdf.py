# Generated by Django 5.0.2 on 2024-11-13 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0021_alter_publications_foto_alter_publications_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publications',
            name='foto',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='publications',
            name='pdf',
            field=models.FileField(blank=True, upload_to='images/%Y/%m/%d'),
        ),
    ]
