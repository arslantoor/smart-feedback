
from urllib import response

from django.core.management.base import BaseCommand
from django.utils import timezone

from feedback_importer import views
from feedback_importer.models import Account

class Command(BaseCommand):
    help = 'Import Forms API'

    def handle(self, *args, **kwargs):
        Accounts = Account.objects.all()
        for account in Accounts:
            views.import_forms('https://sff.coddle.de/api/v2/forms',account.account_id, account.account_password)