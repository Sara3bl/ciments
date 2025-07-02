

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'w-full border border-gray-300 rounded px-3 py-2 bg-white focus:outline-none focus:ring-2 focus:ring-orange-400 placeholder-gray-400',
            'placeholder': 'Email'
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'w-full border border-gray-300 rounded px-3 py-2 bg-white focus:outline-none focus:ring-2 focus:ring-orange-400 placeholder-gray-400',
            'placeholder': "Nom d'utilisateur"
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'w-full border border-gray-300 rounded px-3 py-2 bg-white focus:outline-none focus:ring-2 focus:ring-orange-400 placeholder-gray-400',
            'placeholder': 'Mot de passe'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'w-full border border-gray-300 rounded px-3 py-2 bg-white focus:outline-none focus:ring-2 focus:ring-orange-400 placeholder-gray-400',
            'placeholder': 'Confirmer le mot de passe'
        })

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo', 'prenom', 'nom', 'telephone', 'adresse', 'ville']
        widgets = {
            'prenom': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded px-3 py-2 bg-white focus:outline-none focus:ring-2 focus:ring-orange-400', 'placeholder': 'Prénom'}),
            'nom': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded px-3 py-2 bg-white focus:outline-none focus:ring-2 focus:ring-orange-400', 'placeholder': 'Nom'}),
            'telephone': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded px-3 py-2 bg-white focus:outline-none focus:ring-2 focus:ring-orange-400', 'placeholder': 'Téléphone'}),
            'adresse': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded px-3 py-2 bg-white focus:outline-none focus:ring-2 focus:ring-orange-400', 'placeholder': 'Adresse'}),
            'ville': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded px-3 py-2 bg-white focus:outline-none focus:ring-2 focus:ring-orange-400', 'placeholder': 'Ville'}),
        }
