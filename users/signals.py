from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile

from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
  if created:
    user = instance
    profile = Profile.objects.create(
      user=user,
      email=user.email,
      username=user.username
    )

    subject = "Welcome to Ideas"
    message = "We are so pleased to have you with us!"

    send_mail(
      subject,
      message,
      settings.EMAIL_HOST_USER,
      [profile.email],
      fail_silently=False
    )

@receiver(post_save, sender=Profile)
def updateUser(sender, instance, created, **kwargs):
  profile = instance
  user = profile.user

  if created == False:
    user.username = profile.username
    user.save()

@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
  user = instance.user
  user.delete()
  print("Deleting user..")