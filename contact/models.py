from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from main.models import BaseModel

# Create your models here.
class Contact(BaseModel):
    name=models.CharField(max_length=200,null=True)
    email=models.EmailField(max_length=200,null=True)
    sujet=models.CharField(max_length=200,null=True,blank=True)
    message=models.TextField(null=True)

    class Mata:
        verbose_name="Contact"

    def __str__(self):
        return self.name

    