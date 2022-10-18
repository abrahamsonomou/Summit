from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    list_display=('titre','created',)
    prepopulated_fields={'slug':('titre',)}

@admin.register(Niveau)
class NiveauAdmin(admin.ModelAdmin):
    list_display=('titre','created',)

@admin.register(Personne)
class PersonneAdmin(admin.ModelAdmin):
    list_display=('user','sexe','created',)

@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display=('cours','email','body','created',)

@admin.register(Rapport)
class RapportAdmin(admin.ModelAdmin):
    list_display=('titre','personne','created',)

admin.site.register(Contact)