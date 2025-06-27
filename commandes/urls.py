from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

path('produits-ciment/', views.produits_ciment, name='produits_ciment'),
path('contact/', views.contact, name='contact'),
path('actualités/', views.actualités, name='actualités'),
path('services/', views.services, name='services'),





 

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    



   path('produitdetaille/<int:pk>/', views.produitdetaille, name='produitdetaille'),
   path('initier_paiement/<int:pk>/', views.initier_paiement, name='initier_paiement'),
   path('paiement/', views.paiement, name='paiement'),
   path('telecharger_recu/', views.telecharger_recu, name='telecharger_recu'),

    
   


 
 

     # <-- ajout ici
]


