import json
import requests
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from feedback_importer.models import Form,Question


def index(request):
    return HttpResponse("working")


def import_forms():
    try:
        bulk_size = 10
        url = 'https://sff.coddle.de/api/v2/forms'
        id = 665
        password = "FMJuyuC8uEbo3WxRa5aG"

        headers = {
            'interface-id': str(id),
            'interface-password': password
        }
        json_response = requests.get(url, headers=headers).content
        object = json.loads(json_response)
        for key,value in object.items():
            if isinstance(value, list) or isinstance(value, list):
               for val in value:
                   forms_Records=Form.objects.create(form_id = val.get('form_id'), name = val.get('name'),
                                       type = val.get('type'), completion_rate=val.get('completion_rate'),
                                       open_rate=val.get('open_rate'), is_default = val.get('is_default'),
                                       is_default_form_of_default_survey=val.get('is_default_form_of_default_survey')
                                       )
                   forms_Records.save()

    except Exception as e:
        print("=====model error==\t\t:", str(e))

def import_questions():
    try:
        bulk_size = 10
        param = '6213'
        url = 'https://sff.coddle.de/api/v2/forms/'+param+'/questions'
        id = 665
        password = "FMJuyuC8uEbo3WxRa5aG"

        headers = {
            'interface-id': str(id),
            'interface-password': password
        }
        json_response = requests.get(url, headers=headers).content
        object = json.loads(json_response)
        for key, value in object.items():
            if isinstance(value, list) or isinstance(value, list):
                for val in value:
                    question_record= Question.objects.create(question_id =val.get('question_id'),
                                                             question_label =val.get('question_label'),
                                                             question_type =val.get('question_type'),
                                                             parent_id =val.get('parent_id'),
                                                             is_conditional_question =val.get('is_conditional_question'),
                                                             is_required =val.get('is_required'),
                                                             status =val.get('status'),
                                                             min_range =val.get('min_range'),
                                                             max_range =val.get('max_range'))
                    question_record.save()
    except Exception as e:
        print("=====model error==\t\t:", str(e))