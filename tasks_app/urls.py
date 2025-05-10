from . import views
from django.urls import path
from .views import creer_tache

urlpatterns = [
path ('', views.index, name='index'),
path('taches/', views.taches, name='taches'),
path('creer_tache/', creer_tache, name='creer_tache'),
path('lister_taches/', views.lister_taches, name='lister_taches'),
path('modif_tache/<int:task_id>/', views.modif_tache, name='modif_tache'),
path('supprimer_tache/<int:tache_id>/', views.supprimer_tache, name='supprimer_tache'),


]