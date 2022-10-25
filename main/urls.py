from django.urls import path,include, re_path
from .views import *

from rest_framework import routers
  
# create a router object
router = routers.DefaultRouter()
  
# register the router
router.register(r'cours',CoursView, 'cours')


urlpatterns = [
    path('api/', include(router.urls)),

    path('',home,name='home'),

    #Etudiant
    path('dashboardEtudiant/',dashboardEtudiant,name='dashboardEtudiant'),
    path('profil/',profil,name='profil'),
    path('acceuil/',acceuil,name='acceuil'),
    path('mes_objectifs/',mes_objectifs,name='mes_objectifs'),
    path('mes_cours/',mes_cours,name='mes_cours'),
    path('calendrier/',calendrier,name='calendrier'),
    path('contact/',contact,name='contact'),
    path('discussionPrive/',discussionPrive,name='discussionPrive'),
    path('discussionGroupe/',discussionGroupe,name='discussionGroupe'),
    path('aide/',aide,name='aide'),

    #admin
    path('etudiant/',etudiant,name='etudiant'),
    path('daschboardAdmin/',daschboardAdmin,name='daschboardAdmin'),
    path('cours/',cours,name='cours'),
    path('calendrierAdmin/',calendrierAdmin,name='calendrierAdmin'),
    path('listeMisionnaire/',listeMisionnaire,name='listeMisionnaire'),
    path('voirMissionnaire/',voirMissionnaire,name='voirMissionnaire'),
    path('discussionGroupeAdmin/',discussionGroupeAdmin,name='discussionGroupeAdmin'),
    path('discussionPriveAdmin/',discussionPriveAdmin,name='discussionPriveAdmin'),
    path('ajouterContact/',ajouterContact,name='ajouterContact'),
    path('listeContact/',listeContact,name='listeContact'),
    path('settingEtudiant/',settingEtudiant,name='settingEtudiant'),
    # path('/',,name=''),

    path(r'candidat/',EtudiantList.as_view(),name='Etudiant/'),
    path(r'api/(?P<pk>[0-9]+)/$', EtudiantListDetail.as_view(),name='candidatdetails/'),

    path(r'candidat/',MissionnaireList.as_view(),name='Missionnaire/'),
    path(r'api/(?P<pk>[0-9]+)/$', MissionnaireListDetail.as_view(),name='candidatdetails/'),


    path(r'cours/',CoursList.as_view(),name='cours/'),
    path(r'api/(?P<pk>[0-9]+)/$', CoursListDetail.as_view(),name='coursdetails/'),

    path(r'rapport/',RapportList.as_view(),name='rapport/'),
    path(r'api/(?P<pk>[0-9]+)/$', RapportListDetail.as_view(),name='rapportdetails/'),

    path(r'niveau/',NiveauList.as_view(),name='niveau/'),
    path(r'api/(?P<pk>[0-9]+)/$', NiveauListDetail.as_view(),name='niveaudetails/'),

    path(r'commentaire/',CommentaireList.as_view(),name='commentaire/'),
    path(r'api/(?P<pk>[0-9]+)/$', CommentaireListDetail.as_view(),name='commentairedetails/'),

    path(r'contact/',ContactList.as_view(),name='contact/'),
    path(r'api/(?P<pk>[0-9]+)/$', ContactListDetail.as_view(),name='contactdetails/'),
]