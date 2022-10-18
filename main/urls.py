from django.urls import path,include
from .views import *

from rest_framework import routers
  
# create a router object
router = routers.DefaultRouter()
  
# register the router
router.register(r'cours',CoursView, 'cours')


urlpatterns = [
    path('api/', include(router.urls)),

    path('',home,name='home'),

    path(r'candidat/',PersonneList.as_view(),name='Personne/'),
    path(r'api/(?P<pk>[0-9]+)/$', PersonneListDetail.as_view(),name='candidatdetails/'),

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