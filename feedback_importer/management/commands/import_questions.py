
from urllib import response
from django.core.management.base import BaseCommand
from feedback_importer import views
from feedback_importer.models import Account


class Command(BaseCommand):
    help = 'Import Questions API'

    def handle(self, *args, **kwargs):
        Accounts = Account.objects.all()
        for account in Accounts:
            views.import_questions('https://sff.coddle.de/api/v2/forms/6213/questions',account.account_id, account.account_password)