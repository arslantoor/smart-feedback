from urllib import response

from django.core.management.base import BaseCommand
from django.utils import timezone

from feedback_importer import views
class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, start_date=None,end_date=None, *args, **kwargs):

        start_date = '2019-01-26'
        end_date ='2021-03-30'
        views.import_activity_streams('https://sff.coddle.de/api/v2/forms/activity_stream','665', 'FMJuyuC8uEbo3WxRa5aG',start_date,end_date)