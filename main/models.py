from email.policy import default
from random import choices
from secrets import choice
from django.db import models
from authentication.models import User
import uuid
from django.template.defaultfilters import slugify
from django.urls import reverse
from django_quill.fields import QuillField
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class BaseModel(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')

    class Meta:
        abstract=True

class Niveau(BaseModel):
    titre=models.CharField(max_length=200)

    class Meta:
        verbose_name="Niveau"
        verbose_name_plural="Niveaux"

    def __str__(self) -> str:
        return self.titre

class Cours(BaseModel):
    titre=models.CharField(max_length=100)
    resume=models.TextField(max_length=200,blank=True,null=True)
    contenu=QuillField(blank=True,null=True,max_length=200)
    image=models.ImageField(upload_to='cours',blank=True,null=True)
    niveau=models.ForeignKey(Niveau,on_delete=models.CASCADE,related_name="niveau_cours")
    statut=models.BooleanField(default=False)

    class Meta:
        ordering=['-created']
        verbose_name="Cours"
        verbose_name_plural = 'Cours'

    def __str__(self) -> str:
        return self.titre

class Commentaire(BaseModel):
    cours=models.ForeignKey(Cours,on_delete=models.SET_NULL,null=True,blank=True,related_name='fk_blog_comment')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='comments'
    )
    
    class Meta:
        ordering=['-created']
        verbose_name="Commentaire"


    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name) 

class Rapport(BaseModel):
    titre=models.CharField(max_length=200)
    contenu=models.TextField(blank=True,null=True)
    personne=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Candidat(e)",related_name="rapport_personne")
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Rapport'
        verbose_name_plural = 'Rapports'
    
    def __str__(self) -> str:
        return self.titre

class Jour(BaseModel):
    titre=models.CharField(max_length=200)

    class Meta:
        verbose_name="Jour"

    def __str__(self) -> str:
        return self.titre

class Objectif(BaseModel):
    titre=models.CharField(max_length=100)
    contenu=models.TextField(max_length=200,blank=True,null=True)
    etudiant=models.ForeignKey(User,on_delete=models.CASCADE)
    jour=models.ForeignKey(Jour,on_delete=models.CASCADE)
    heure=models.TimeField(max_length=100)

    class Meta:
        ordering=['-created']
        verbose_name="Objectif"
        verbose_name_plural = 'Objectifs'

    def __str__(self) -> str:
        return self.titre

# Contact
class Contact(BaseModel):
    nom=models.CharField(blank=True,null=True,max_length=100,name='nom',verbose_name='Nom')
    email=models.EmailField(blank=True,null=True,max_length=100,name='email',verbose_name='Email')
    sujet=models.CharField(blank=True,null=True,max_length=100,name='sujet',verbose_name='Sujet')
    message=models.TextField(blank=True,null=True,verbose_name='Message',name='message')
    
    class Meta:
        ordering=['-created']
        verbose_name="Contact" 

    def __str__(self) -> str:
        return self.nom

        
