from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Tache

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

def taches(request):
    utilisateur = request.user
    taches = Tache.objects.filter(utilisateur=utilisateur)
    return render(request, 'taches.html', {'tasks': taches})