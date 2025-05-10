from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import TacheForm
from .models import Tache
from datetime import datetime
from django.db.models import Q

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

def taches(request):
    utilisateur = request.user
    taches = Tache.objects.filter(utilisateur=utilisateur)
    return render(request, 'taches.html', {'tasks': taches})

def creer_tache(request):
    if request.method == 'POST':
        form = TacheForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            statut = form.cleaned_data['statut']
            utilisateur = form.cleaned_data['utilisateur']

            # Vérifier s’il existe déjà une tâche assignée au même utilisateur sur le même créneau
            if Tache.objects.filter(
                utilisateur=utilisateur,
                start_date__lt=end_date,
                end_date__gt=start_date
            ).exists():
                return HttpResponse("Une autre tâche est déjà prévue pour cet utilisateur sur ce créneau horaire.")

            # Créer la tâche
            Tache.objects.create(
                name=name,
                start_date=start_date,
                end_date=end_date,
                statut=statut,
                utilisateur=utilisateur
            )
            return redirect('index')  # Redirige vers une page d’accueil ou de confirmation
    else:
        form = TacheForm()
    return render(request, 'creer_tache.html', {'form': form})

@login_required
def lister_taches(request):
    # Récupère toutes les tâches de l'utilisateur connecté
    taches = Tache.objects.filter(utilisateur=request.user)
    
    # Passe les tâches dans le contexte pour les afficher dans le template
    return render(request, 'lister_taches.html', {'taches': taches})


@login_required
def modif_tache(request, task_id):
    task = get_object_or_404(Tache, id=task_id)  # Récupérer la tâche par son ID

    if request.method == 'POST':
        form = TacheForm(request.POST, instance=task)  # Remplir le formulaire avec les données de la tâche existante
        if form.is_valid():
            name = form.cleaned_data['name']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            statut = form.cleaned_data['statut']
            utilisateur = form.cleaned_data['utilisateur']

            # Vérifier s’il existe déjà une tâche assignée au même utilisateur sur le même créneau
            if Tache.objects.filter(
                utilisateur=utilisateur,
                start_date__lt=end_date,
                end_date__gt=start_date
            ).exclude(id=task.id).exists():  # Ne pas tenir compte de la tâche en cours (celle qu'on modifie)
                return HttpResponse("Une autre tâche est déjà prévue pour cet utilisateur sur ce créneau horaire.")

            # Mettre à jour la tâche
            task.name = name
            task.start_date = start_date
            task.end_date = end_date
            task.statut = statut
            task.utilisateur = utilisateur
            task.save()

            return redirect('lister_taches')  # Redirige vers la liste des tâches
    else:
        form = TacheForm(instance=task)  # Pré-remplir le formulaire avec les données de la tâche existante

    return render(request, 'modif_tache.html', {'form': form})


def supprimer_tache(request, tache_id):
    tache = get_object_or_404(Tache, id=tache_id)
    tache.delete()
    return redirect('index')
