from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',login_view,name='login'),
    path('register/',register_user,name='register'),
    path('forgot_password',forgot_password,name='forgot_password'),
    path("logout/", LogoutView.as_view(), name="logout")
]