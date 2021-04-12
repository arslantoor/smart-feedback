import json
import requests
from collections import defaultdict
from django.apps import apps
# from django.db import utils
import utils
from django.core.serializers import serialize
from django.utils import timezone
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils import timezone

from feedback_importer import models
from feedback_importer.models import Form, Question, Test


def index(request):
    return render(request, "index.html")


def importer_commands(request):
    if request.method == 'POST':
        importer_type=request.POST['importer_type']
        url=request.POST['url']
        header_key=request.POST['header_key']
        header_value=request.POST['header_value']
        param_key=request.POST['param_key']
        param_value=request.POST['param_value']
        if importer_type == "1":
            import_forms(url,header_key,header_value)
            print("==============\t\t:==\t",importer_type)
        elif importer_type == "2":
            import_questions(url,header_key,header_value)
        elif importer_type == "3":
            import_answers(url,header_key,header_value)
        elif importer_type == "4":
            import_activity_streams(url,header_key,header_value)

    return render(request, 'index.html')



def import_forms(url,header_key,header_value):
    try:
        bulk_size = 10
        url = url
        id = header_key
        password = header_value

        headers = {
            'interface-id': id,
            'interface-password': password
        }
        json_response = requests.get(url, headers=headers).content
        object = json.loads(json_response)
        for key,value in object.items():
            if isinstance(value, list) or isinstance(value, list):
                instances = [
                    models.Form(
                        form_id = val.get('form_id'), name = val.get('name'),
                        type = val.get('type'), completion_rate=val.get('completion_rate'),
                        open_rate=val.get('open_rate'), is_default = val.get('is_default'),
                        is_default_form_of_default_survey=val.get('is_default_form_of_default_survey')
                        )
                    for val in value
                ]
                models.Form.objects.bulk_create(instances)
    except Exception as e:
        print("=====model insertion error==\t\t:", str(e))

def import_questions(url,header_key,header_value):
    try:
        bulk_size = 10
        url = url
        id = header_key
        password = header_value

        headers = {
            'interface-id': str(id),
            'interface-password': password
        }
        json_response = requests.get(url, headers=headers).content
        object = json.loads(json_response)
        for key, value in object.items():
            if isinstance(value, list) or isinstance(value, list):
                instances = [
                    models.Question(question_id =val.get('question_id'),
                    question_label =val.get('question_label'),
                    question_type =val.get('question_type'),
                    parent_id =val.get('parent_id'),
                    is_conditional_question =val.get('is_conditional_question'),
                    is_required =val.get('is_required'),
                    status =val.get('status'),
                    min_range =val.get('min_range'),
                    max_range =val.get('max_range'))
                    for val in value
                ]
            models.Question.objects.bulk_create(instances)
    except Exception as e:
        print("=====import error==\t\t:", str(e))


def import_answers(url,header_key,header_value):
    try:
        bulk_size = 10
        url = url
        id = header_key
        password = header_value
        headers = {
            'interface-id': id,
            'interface-password': password
        }
        json_response = requests.get(url, headers=headers).content
        json_response =json.loads(json_response)
        for obj in json_response.items():
            for t in obj:
                if isinstance(t,tuple):
                    print("t1====",t)
                elif isinstance(t, str):
                    print("t2====",t)
                elif isinstance(t, dict):
                    dicRecord=t.get('result')
                    print("t3====",dicRecord['shop_id'])
                elif isinstance(t, int):
                    print("t4====",t)



    except Exception as e:
        print("=====model error==\t\t:", str(e))


def import_activity_streams():
    pass


# Testing code working on.
def orm_create(n_records):
    for i in range(0, n_records):
        models.Test.objects.create(
            field_1=i,
            field_2=str(i),
            field_3=timezone.now(),
        )

if __name__ == '__main__':
    utils.timed(orm_create)

def orm_bulk_create(n_records):
    instances = [
        models.Test(
            field_1=i,
            field_2=str(i),
            field_3=timezone.now(),
        )
        for i in range(0, n_records)

    ]
    print(len(instances))
    for a in instances:
        print(a)
    queryset = models.Test.objects.bulk_create(instances)
    # Modify query string with explain syntax

    return queryset