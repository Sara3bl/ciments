from django.shortcuts import render
from .models import Produit  # Assure-toi que ce modèle existe

def home(request):
    produits = Produit.objects.all()  # Récupère les produits depuis la BDD
    return render(request, 'commandes/home.html', {'produits': produits})
from django.shortcuts import render
from .models import Produit



from django.shortcuts import render

def produits_ciment(request):
    produits = Produit.objects.all()
    return render(request, 'commandes/produits-ciment.html', {'produits': produits})
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        entreprise = request.POST.get('entreprise')
        sujet = request.POST.get('sujet')
        message = request.POST.get('message')
        contenu = f"Nom: {nom}\nEmail: {email}\nTéléphone: {telephone}\nEntreprise: {entreprise}\nSujet: {sujet}\nMessage:\n{message}"
        send_mail(
            subject=f'Nouveau message contact: {sujet}',
            message=contenu,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['Benserrou@gmail.com'],
            fail_silently=False,
        )
        messages.success(request, "Votre message a été envoyé avec succès.")
        return render(request, 'commandes/contact.html', {"success": True})
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
from django.shortcuts import get_object_or_404

def produitdetaille(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    return render(request, 'produitdetaille.html', {'produit': produit})

from django.shortcuts import redirect
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from .models import Paiement


def telecharger_recu(request):
    # Récupérer le dernier paiement effectué (pour une vraie app, filtrer par user/session)
    paiement = Paiement.objects.last()
    if not paiement:
        return HttpResponse("Aucun paiement trouvé.", content_type="text/plain")

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="recu_paiement.pdf"'

    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    # Add logo on the left
    logo_path = 'media/produits/logo.png'
    logo_width = 180
    logo_height = 40
    logo_x = 50
    logo_y = height - 110
    try:
        p.drawImage(logo_path, logo_x, logo_y, width=logo_width, height=logo_height, mask='auto')
    except Exception as e:
        p.setFont("Helvetica", 8)
        p.drawString(logo_x, logo_y + 15, "[Logo introuvable]")

    # Header title centered at the top
    p.setFont("Helvetica-Bold", 22)
    title_text = "Reçu de Paiement"
    title_width = p.stringWidth(title_text, "Helvetica-Bold", 22)
    title_x = (width - title_width) / 2
    # Place title high enough so it doesn't overlap the logo
    title_y = height - 60
    p.drawString(title_x, title_y, title_text)

    # Add extra vertical space below header before the horizontal line
    line_y = height - 140
    p.setLineWidth(1)
    p.line(50, line_y, width - 50, line_y)

    # Receipt details
    p.setFont("Helvetica", 13)
    y = height - 170
    line_height = 28
    p.drawString(60, y, f"Nom: {paiement.nom}")
    y -= line_height
    p.drawString(60, y, f"Email: {paiement.email}")
    y -= line_height
    p.drawString(60, y, f"Adresse: {paiement.adresse}")
    y -= line_height
    p.drawString(60, y, f"Ville: {paiement.ville}")
    y -= line_height
    p.drawString(60, y, f"Code Postal: {paiement.code_postal}")
    y -= line_height
    p.drawString(60, y, f"Téléphone: {paiement.telephone}")
    y -= line_height
    p.setFont("Helvetica-Bold", 14)
    p.drawString(60, y, f"Montant payé: {paiement.montant} DH")
    y -= line_height
    from datetime import timedelta
    date_affichee = paiement.date_paiement + timedelta(hours=1) if paiement.date_paiement else None
    p.setFont("Helvetica", 13)
    p.drawString(60, y, f"Date: {date_affichee.strftime('%d/%m/%Y %H:%M') if date_affichee else ''}")

    # Footer message
    y -= line_height * 2
    p.setFont("Helvetica-Oblique", 12)
    p.setFillColorRGB(0.8, 0.4, 0.1)
    p.drawString(60, y, "Merci pour votre confiance !")
    p.setFillColorRGB(0, 0, 0)

    p.showPage()
    p.save()
    return response

def initier_paiement(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    # Récupère la quantité depuis GET ou POST (par défaut 1)
    try:
        quantite = int(request.GET.get('quantite', 1))
    except (TypeError, ValueError):
        quantite = 1
    montant = float(produit.prix_unitaire) * quantite
    request.session['montant'] = montant
    return redirect('paiement')


from .models import Paiement

def paiement(request):
    # Exemple : calcul du montant à partir du panier stocké en session
    montant = request.session.get('montant', 0)
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        adresse = request.POST.get('adresse')
        ville = request.POST.get('ville')
        code_postal = request.POST.get('code_postal')
        telephone = request.POST.get('telephone')
        # montant pris côté serveur
        Paiement.objects.create(
            nom=nom,
            email=email,
            adresse=adresse,
            ville=ville,
            code_postal=code_postal,
            telephone=telephone,
            montant=montant
        )
        return render(request, 'paiement_succes.html')
    return render(request, 'paiement.html', {'montant': montant})
