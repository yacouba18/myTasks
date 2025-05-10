from django import forms
from .models import Tache
from django.contrib.auth.models import User

class TacheForm(forms.ModelForm):
    start_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'datetime-local'
        }),
        required=False
    )
    end_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'datetime-local'
        }),
        required=False
    )

    class Meta:
        model = Tache
        fields = ['name', 'start_date', 'end_date', 'statut', 'utilisateur']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'statut': forms.Select(attrs={'class': 'form-control'}),
            'utilisateur': forms.Select(attrs={'class': 'form-control'}),
        }
