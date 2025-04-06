from django.db import models
from django.contrib.auth.models import User

class Tache(models.Model):
    id = models.AutoField(primary_key=True)  # Identifiant unique pour chaque tâche
    
    # Nom de la tâche
    name = models.CharField(max_length=255, null=True, blank=True)
    
    # Date de début de la tâche
    start_date = models.DateTimeField(null=True, blank=True)
    
    # Date de fin souhaitée de la tâche
    end_date = models.DateTimeField(null=True, blank=True)
    
    # Statut de la tâche
    STATUT_CHOICES = [

        ('pas_debutee', 'Pas debutée'),
        ('en_cours', 'En cours'),
        ('termine', 'Terminée'),
        ('en_retard', 'En retard'),
    ]
    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='pas_debutee',
    )
    
# Utilisateur assigné à la tâche (un seul utilisateur)
    utilisateur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='taches')

    class Meta:
        db_table = "taches"  # Nom de la table dans la base de données
