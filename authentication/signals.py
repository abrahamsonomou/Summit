from django.db.models.signals import post_save
from.models import User, Missionnaire, Etudiant
from django.dispatch import receiver


def save_profile(sender, instance, created, **kwargs):
	if created:
		if instance.is_etudiant:
			etudiant = Etudiant(user=instance)
			etudiant.save()
		elif instance.is_missionnaire:
			missionnaire = Missionnaire(user=instance)
			missionnaire.save()


post_save.connect(save_profile, sender=User)