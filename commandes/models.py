from django.db import models
from django.contrib.auth.models import User

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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profiles/', blank=True, null=True)
    prenom = models.CharField(max_length=100, blank=True)
    nom = models.CharField(max_length=100, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    adresse = models.CharField(max_length=255, blank=True)
    ville = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

class Paiement(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    adresse = models.CharField(max_length=255)
    ville = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=10)
    telephone = models.CharField(max_length=20)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_paiement = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.montant} DH"
