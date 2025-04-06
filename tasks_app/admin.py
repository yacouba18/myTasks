from django.contrib import admin
from .models import Tache

class TacheAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        # Vérifiez si l'utilisateur est un superutilisateur ou s'il a la permission 'can_view_all_tasks'
        if request.user.is_superuser or request.user.has_perm('tasks.can_view_all_tasks'):
            return True
        return False

admin.site.register(Tache, TacheAdmin)
