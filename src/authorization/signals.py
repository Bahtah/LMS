from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from authorization.models import Role

User = get_user_model()

@receiver(post_save, sender=User)
def assign_admin_role_to_superusers(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        admin_role, created = Role.objects.get_or_create(
            name='ADMIN',
            defaults={'description': 'Administrator with full access'}
        )
        instance.roles.add(admin_role)