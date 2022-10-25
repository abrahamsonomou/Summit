from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
from authentication.models import *

#serialisation de la classe Niveau
class NiveauSerializer(ModelSerializer):
    class Meta:
        model=Niveau
        fields='__all__' 

#serialisation de la classe Etudiant
class EtudiantSerializer(ModelSerializer):
    class Meta:
        model=Etudiant
        fields='__all__'

#serialisation de la classe Missionnaire
class MissionnaireSerializer(ModelSerializer):
    class Meta:
        model=Missionnaire
        fields='__all__'

#serialisation de la classe Cours
class CoursSerializer(ModelSerializer):
    class Meta:
        model=Cours
        fields='__all__'

#serialisation de la classe Commentaire
class CommentaireSerializer(ModelSerializer):
    class Meta:
        model=Commentaire
        fields='__all__' 

#serialisation de la classe Rapport
class RapportSerializer(ModelSerializer):
    class Meta:
        model=Rapport
        fields='__all__' 

#serialisation de la classe Contact
class ContactSerializer(ModelSerializer):
    class Meta:
        model=Contact
        fields=['nom','email','sujet','message'] 