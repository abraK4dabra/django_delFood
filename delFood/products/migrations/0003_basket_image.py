# Generated by Django 5.1.1 on 2024-10-30 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_fooditem'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='image',
            field=models.ImageField(blank=True, upload_to='products_images'),
        ),
    ]
