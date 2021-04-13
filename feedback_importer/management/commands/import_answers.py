from urllib import response

from django.core.management.base import BaseCommand
from django.utils import timezone

from feedback_importer import views
class Command(BaseCommand):
    help = 'Import Answers API'

    def handle(self, *args, **kwargs):
        views.import_answers('https://sff.coddle.de/api/v3/answers/','665', 'FMJuyuC8uEbo3WxRa5aG')
        # views.orm_create(5)
        # views.orm_bulk_create(5)
