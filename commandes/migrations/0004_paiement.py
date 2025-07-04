# Generated by Django 5.2 on 2025-06-27 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commandes', '0003_produit_applications_produit_avantages_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('adresse', models.CharField(max_length=255)),
                ('ville', models.CharField(max_length=100)),
                ('code_postal', models.CharField(max_length=10)),
                ('telephone', models.CharField(max_length=20)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_paiement', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
