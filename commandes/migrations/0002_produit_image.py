# Generated by Django 5.2 on 2025-06-27 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commandes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='produits/'),
        ),
    ]
