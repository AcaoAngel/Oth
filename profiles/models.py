from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, 
                                    on_delete=models.CASCADE,#When user deleted profile should be deleted too
                                    null=False, blank=False)#This line tells that cant be a profile without a user
    bio = models.CharField(max_length=255, blank=True)
    web = models.URLField(blank=True)

    def __str__(self): 
        return self.user.username

@receiver(post_save, sender=User)#<---indicates that the function is a receiver of a signal: https://adriennedomingus.com/blog/signals-in-django
def create_profile_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)#<---indicates that the function is a receiver of a signal: https://adriennedomingus.com/blog/signals-in-django
def save_profile_user(sender, instance, **kwargs):
    instance.profile.save()
