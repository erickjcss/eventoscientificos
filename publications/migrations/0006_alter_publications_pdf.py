# Generated by Django 5.0.2 on 2024-03-02 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0005_alter_publications_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publications',
            name='pdf',
            field=models.FileField(blank=True, upload_to='pdfs/'),
        ),
    ]
