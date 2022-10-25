from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    def create_user(self,email,username,password=None,*callback_args, **callback_kwargs):
        
        if not email:
            raise ValueError('Desolé, veuillez saisir un email')
        
        email=self.normalize_email(email)
        user=self.model(email=email,username=username)
        
        user.set_password(password)
        
        # user=self.model(username=username,password=password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,password):
        user=self.create_user(email,username,password)
        
        user.is_staff=True
        user.is_superuser=True
        
        user.save(using=self._db)
        return user   
    
class User(AbstractUser):
    CHOIX_CIVILITE=(
    ('celibataire','Celibataire'),
    ('marie','Marié(e)'),
    ('divorce','divorcé(e)',)
    )
    telephone=PhoneNumberField(null=True,blank=True,unique=True)
    civilite=models.CharField(choices=CHOIX_CIVILITE,default='celibataire', blank=True,null=True,max_length=200)
    profession=models.CharField(blank=True,null=True,max_length=200)
    addresse=models.CharField(blank=True,null=True,max_length=200)
    
    description=models.TextField(blank=True,null=True)
    twitter=models.CharField(blank=True,null=True,name='twitter',verbose_name="Twitter",max_length=200)
    facebook=models.CharField(blank=True,null=True,name='facebook',verbose_name="Facebook",max_length=200)
    instagram=models.CharField(blank=True,null=True,name='instagram',verbose_name="Instagram",max_length=200)
    linkdin=models.CharField(blank=True,null=True,name='linkdin',verbose_name="Linkdin",max_length=200)
   
    is_etudiant = models.BooleanField(default=True)
    is_missionnaire = models.BooleanField(default=False)
   
    email = models.EmailField('email address', unique=True)
    username = models.CharField(max_length=30, unique=True)
    photo = models.ImageField(upload_to='users/photos/', null=True,blank=True)
    
    USERNAME_FIELD='username'
    # REQUIRED_FIELDS=['username']
    
    def __str__(self):
        if self.is_etudiant:
            type_ = 'Etudiant'
        elif self.is_missionnaire:
            type_ = 'Missionnaire'
        elif self.is_superuser:
            type_ = 'Admin'
        else:
            type_ = 'None'
        return f'{type_}: {self.email}'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            pic = Image.open(self.photo.path)
            if pic.width > 256:
                pic.thumbnail((256, pic.height / (pic.width / 265)))
                pic.save(self.photo.path)
    
    def get_photo_url(self):
        if self.photo:
            return self.photo.url
        else:
            if self.is_etudiant:
                return '/media/users/photos/etudiant-default.png'
            elif self.is_missionnaire:
                return '/media/users/photos/missionnaire-default.png'
            else:
                return '/media/users/photos/default.png'
        
    def get_photo_name(self):
        if self.photo:
            return self.photo.name
        else:
            if self.is_student:
                return 'student.png'
            elif self.is_teacher:
                return 'teacher.png'
            else:
                return 'default.png'
    
    def get_profile(self):
        if self.is_student:
            return Etudiant.objects.get(user=self)
        elif self.is_teacher:
            return Missionnaire.objects.get(user=self)
        else:
            return None
    
    def get_shortname(self):
        return f'{self.first_name[0:1]}.{self.last_name}'
        
    def get_fullname(self):
        return f'{self.first_name} {self.last_name}'

    objects= UserProfileManager()

class Etudiant(models.Model):
    date_conversion=models.DateField(blank=True,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, unique=True)


    def __str__(self) -> str:
        return self.user.username	

class Missionnaire(models.Model):
    date_engagement=models.DateField(blank=True,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, unique=True)

    def __str__(self) -> str:
        return f'{self.user.username} {self.user.email}'	