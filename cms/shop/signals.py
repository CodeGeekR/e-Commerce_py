from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from allauth.account.signals import user_signed_up
from django.contrib.auth import get_user_model
from .models import Profile


@receiver(post_save, sender=Profile)
def create(sender, instance, **kwargs):
    if create:
        try:
            group = Group.objects.get(name='Clientes')
        except Group.DoesNotExist:
            group = Group.objects.create(name='Clientes')
        instance.user.groups.add(group)

