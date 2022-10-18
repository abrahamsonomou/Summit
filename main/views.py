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

# import view sets from the REST framework
from rest_framework import viewsets

# Create your views here.
class CoursView(viewsets.ModelViewSet):
    serializer_class = CoursSerializer
    queryset = Cours.objects.all()

@login_required
def home(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('pages/index.html')
    return HttpResponse(html_template.render(context, request))

# def home(request):
#     return render(request,"pages/home.html")



class PersonneList(generics.ListCreateAPIView):
    queryset=Personne.objects.all()
    serializer_class=PersonneSerializer
    permission_classes = [IsAdminUser]
    
class PersonneListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Personne.objects.all()
    serializer_class=PersonneSerializer
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
    