
from urllib import response
from django.core.management.base import BaseCommand
from feedback_importer import views


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        views.import_questions()