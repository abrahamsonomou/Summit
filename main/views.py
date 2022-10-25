from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from .serializers import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django import template

# import view sets from the REST framework
from rest_framework import viewsets

# Create your views here.
@login_required
def home(request):
    return render(request,'pages/index.html')

@login_required()
def dashboardEtudiant(request):
    return render(request,"etudiant/dashboardEtudiant.html")

@login_required()
def  profil(request):
    return render(request,"etudiant/profil.html")

@login_required()
def  mes_objectifs(request):
    return render(request,"etudiant/mes_objectifs.html")

@login_required()
def  mes_cours(request):
    return render(request,"etudiant/mes_cours.html")

@login_required()
def  contact(request):
    return render(request,"etudiant/contact.html")

@login_required()
def  calendrier(request):
    return render(request,"etudiant/calendrier.html")

@login_required()
def  aide(request):
    return render(request,"etudiant/aide.html")

@login_required()
def  discussionPrive(request):
    return render(request,"etudiant/discussion/discussionPrive.html")

@login_required()
def  discussionGroupe(request):
    return render(request,"etudiant/discussion/discussionGroupe.html")

@login_required()
def settingEtudiant(request):
    return render(request,"etudiant/settingEtudiant.html")

#admin
@login_required()
def etudiant(request):
    # etudiants=User.objects.filter(is_etudiant=True)
    etudiants=Etudiant.objects.all()
    context={
        'etudiants':etudiants
    }
    return render(request,"admin/etudiant.html",context) 

@login_required()
def daschboardAdmin(request):
    return render(request,"admin/daschboardAdmin.html")

@login_required()
def cours(request):
    return render(request,"admin/cours.html")


@login_required()
def calendrierAdmin(request):
    return render(request,"admin/calendrierAdmin.html")

@login_required()
def listeMisionnaire(request):
    missionnaires=Missionnaire.objects.all()
    context={
        'missionnaires':missionnaires
    }
    return render(request,"admin/misionnaire/listeMisionnaire.html",context)

@login_required()
def voirMissionnaire(request):
    return render(request,"admin/misionnaire/voirMissionnaire.html")

@login_required()
def discussionGroupeAdmin(request):
    return render(request,"admin/discussion/discussionGroupeAdmin.html")

@login_required()
def discussionPriveAdmin(request):
    return render(request,"admin/discussion/discussionPriveAdmin.html")

@login_required()
def ajouterContact(request):
    return render(request,"admin/contact/ajouterContact.html")

@login_required()
def listeContact(request):
    return render(request,"admin/contact/listeContact.html")




@login_required()
def acceuil(request):
    return render(request,"pages/acceuil.html")    




class CoursView(viewsets.ModelViewSet):
    serializer_class = CoursSerializer
    queryset = Cours.objects.all()


#rest framework
class MissionnaireList(generics.ListCreateAPIView):
    queryset=Missionnaire.objects.all()
    serializer_class=MissionnaireSerializer
    permission_classes = [IsAdminUser]
    
class MissionnaireListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Missionnaire.objects.all()
    serializer_class=MissionnaireSerializer
    permission_classes = [IsAdminUser]

class EtudiantList(generics.ListCreateAPIView):
    queryset=Etudiant.objects.all()
    serializer_class=EtudiantSerializer
    permission_classes = [IsAdminUser]
    
class EtudiantListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Etudiant.objects.all()
    serializer_class=EtudiantSerializer
    permission_classes = [IsAdminUser]

class CoursList(generics.ListCreateAPIView):
    queryset=Cours.objects.all()
    serializer_class=CoursSerializer
    permission_classes = [IsAdminUser]
    
class CoursListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Cours.objects.all()
    serializer_class=CoursSerializer
    permission_classes = [IsAdminUser]

class NiveauList(generics.ListCreateAPIView):
    queryset=Niveau.objects.all()
    serializer_class=NiveauSerializer
    permission_classes = [IsAdminUser]
    
class NiveauListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Niveau.objects.all()
    serializer_class=NiveauSerializer
    permission_classes = [IsAdminUser]

class CommentaireList(generics.ListCreateAPIView):
    queryset=Commentaire.objects.all()
    serializer_class=CommentaireSerializer
    permission_classes = [IsAdminUser]
    
class CommentaireListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Commentaire.objects.all()
    serializer_class=CommentaireSerializer
    permission_classes = [IsAdminUser]

class RapportList(generics.ListCreateAPIView):
    queryset=Rapport.objects.all()
    serializer_class=RapportSerializer
    permission_classes = [IsAdminUser]
    
class RapportListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Rapport.objects.all()
    serializer_class=RapportSerializer
    permission_classes = [IsAdminUser]

class ContactList(generics.ListCreateAPIView):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer
    
class ContactListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer    
    