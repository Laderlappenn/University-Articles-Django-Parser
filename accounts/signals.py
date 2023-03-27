from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Account
from acts.models import Table_1


@receiver(post_save, sender=Table_1)
def update_account_date_updated(sender, instance, **kwargs):
    account = Account.objects.filter(table_1=instance).first()
    if account:
        account.date_updated = instance.date_updated
        account.save()