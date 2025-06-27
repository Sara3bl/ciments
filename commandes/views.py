from django.shortcuts import render
from .models import Produit  # Assure-toi que ce modèle existe

def home(request):
    produits = Produit.objects.all()  # Récupère les produits depuis la BDD
    return render(request, 'commandes/home.html', {'produits': produits})
from django.shortcuts import render
from .models import Produit



from django.shortcuts import render

def produits_ciment(request):
    return render(request, 'commandes/produits-ciment.html')
def contact(request):
    return render(request, 'commandes/contact.html')
def actualités(request):
    return render(request, 'commandes/actualités.html')
def services(request):
    return render(request, 'commandes/services.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'commandes/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')  # à créer ou adapter
        else:
            return render(request, 'commandes/login.html', {'error': 'Nom ou mot de passe incorrect'})
    return render(request, 'commandes/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
def produitdetaille(request):
    return render(request, 'produitdetaille.html')

def paiement(request):
    return render(request, 'paiement.html')
