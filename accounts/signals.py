from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Account
from acts.models import Act


@receiver(post_save, sender=Act)
def update_account_date_updated(sender, instance, **kwargs):
    account = Account.objects.filter(act=instance).first()
    if account:
        account.date_updated = instance.date_updated
        account.save()