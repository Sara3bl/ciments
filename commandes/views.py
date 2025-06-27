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

from django.http import JsonResponse
from django.template.loader import render_to_string

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # Si AJAX, renvoyer le formulaire login HTML
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                login_html = render_to_string('commandes/login.html', {}, request=request)
                return JsonResponse({'success': True, 'login_html': login_html})
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
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            return redirect('home')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                login_html = render_to_string('commandes/login.html', {'error': 'Nom ou mot de passe incorrect'}, request=request)
                return JsonResponse({'success': False, 'login_html': login_html})
            return render(request, 'commandes/login.html', {'error': 'Nom ou mot de passe incorrect'})
    return render(request, 'commandes/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')
def produitdetaille(request):
    return render(request, 'produitdetaille.html')

def paiement(request):
    return render(request, 'paiement.html')
