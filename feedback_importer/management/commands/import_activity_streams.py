from urllib import response

from django.core.management.base import BaseCommand
from django.utils import timezone

from feedback_importer import views
from feedback_importer.models import Account

class Command(BaseCommand):
    help = 'Import Activity Streams'

    def handle(self, start_date=None,end_date=None, *args, **kwargs):

        start_date = input('Enter Start Date (2019-01-26)')
        end_date =input('Enter End Data (2021-03-30)')
        Accounts = Account.objects.all()
        for account in Accounts:
            views.import_activity_streams('https://sff.coddle.de/api/v2/forms/activity_stream',account.account_id, account.account_password,start_date,end_date)