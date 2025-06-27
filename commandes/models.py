from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix_unitaire = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='produits/', blank=True, null=True)
    caracteristiques = models.TextField(blank=True, null=True, help_text="Caractéristiques principales du produit")
    avantages = models.TextField(blank=True, null=True, help_text="Avantages du produit (une ligne par avantage)")
    applications = models.TextField(blank=True, null=True, help_text="Applications principales (une ligne par application)")
    classe = models.CharField(max_length=50, blank=True, null=True, help_text="Classe du ciment, ex: CPJ 35")
    poids = models.CharField(max_length=50, blank=True, null=True, help_text="Poids par sac, ex: 50 kg")
    resistance = models.CharField(max_length=100, blank=True, null=True, help_text="Résistance, ex: ≥ 22.5 MPa")
    temps_prise = models.CharField(max_length=100, blank=True, null=True, help_text="Temps de prise, ex: 2-6 heures")

    def __str__(self):
        return self.nom
