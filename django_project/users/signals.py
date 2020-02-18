from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# when a User is saved, send this signal
# this signal will be received by receiver (this function)
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # this function receives all args that post_save signal passes to it
    # one of those is the instance of the User, one is created
    if created:
        # if that User was created, then create a Profile object
        # with the user equals to the instance of the created User
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
