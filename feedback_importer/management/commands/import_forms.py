
from urllib import response

from django.core.management.base import BaseCommand
from django.utils import timezone

from feedback_importer import views
class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        views.import_forms('https://sff.coddle.de/api/v2/forms','665', 'FMJuyuC8uEbo3WxRa5aG')