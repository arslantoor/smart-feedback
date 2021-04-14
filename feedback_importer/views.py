import json
import requests
from django.shortcuts import render
from feedback_importer import models
from feedback_importer.models import Form, Question, Test,ActivityStream,Answer
from django.utils import timezone
from collections import defaultdict
from django.apps import apps
# from django.db import utils
import utils
from django.core.serializers import serialize
from django.utils import timezone
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


def importer_commands(request):
    if request.method == 'POST':

        importer_type = request.POST['importer_type']
        url = request.POST['url']
        header_key = request.POST['header_key']
        header_value = request.POST['header_value']
        param_key = request.POST['param_key']
        param_value = request.POST['param_value']

        if importer_type == "1":
            import_forms(url,header_key,header_value)

        elif importer_type == "2":
            import_questions(url,header_key,header_value)

        elif importer_type == "3":
            import_answers(url,header_key,header_value)

        elif importer_type == "4":
            import_activity_streams(url,header_key,header_value,param_key,param_value)

    return render(request, 'index.html')


def import_forms(api_request_url,api_request_header_id,api_request_header_password):
    try:
        headers = {
            'interface-id': api_request_header_id,
            'interface-password': api_request_header_password
        }
        json_response = requests.get(api_request_url, headers=headers).content
        object = json.loads(json_response)
        #  Iterate over objects keys and values pairs
        for key,value in object.items():
            if isinstance(value, list) or isinstance(value, dict):
                # create each queryset instance list
                instances = [
                    models.Form(
                        form_id=val.get('form_id'), name=val.get('name'),
                        type=val.get('type'), completion_rate=val.get('completion_rate'),
                        open_rate=val.get('open_rate'), is_default = val.get('is_default'),
                        is_default_form_of_default_survey=val.get('is_default_form_of_default_survey')
                        )
                    for val in value
                ]
            models.Form.objects.bulk_create(instances)
    except Exception as e:
        print("== Import Exceptions ==\t\t:", str(e))


def import_questions(api_request_url,api_request_header_id,api_request_header_password):
    try:
        instances=[]
        headers = {
            'interface-id': api_request_header_id,
            'interface-password': api_request_header_password
        }
        json_response = requests.get(api_request_url, headers=headers).content
        object = json.loads(json_response)
        #  Iterate over objects keys and values pairs
        for keys, values in object.items():
            if isinstance(values, list) or isinstance(values, dict):
                # create each queryset instance list
                instances = [
                    models.Question(
                        question_id =value.get('question_id'),
                        question_label =value.get('question_label'),
                        question_type =value.get('question_type'),
                        parent_id =value.get('parent_id'),
                        is_conditional_question =value.get('is_conditional_question'),
                        is_required =value.get('is_required'),
                        status =value.get('status'),
                        min_range =value.get('min_range'),
                        max_range =value.get('max_range')
                    )
                    for value in values
                ]
            models.Question.objects.bulk_create(instances)
    except Exception as e:
        print("== Import Exceptions ==\t\t:", str(e))

#  Check dictionary method from import_answer


def import_activity_streams(api_request_url,api_request_header_id,api_request_header_password,param_key,param_value):
    try:
        # set api request header
        headers = {
            'interface-id': api_request_header_id,
            'interface-password': api_request_header_password
        }
        # set api request url parameters
        url_parameter = {
            'start_date':param_key,
            'end_date':param_value
        }
        json_response = requests.get(api_request_url,url_parameter, headers=headers).content
        object = json.loads(json_response)

        #  Iterate over objects keys and values pairs
        for keys, values in object.items():
            if isinstance(values, list) or isinstance(values, dict):
                # create each queryset instance list
                instances = [
                    models.ActivityStream(
                        form_key=value.get('form_key'),
                        order_id=value.get('order_id'),
                        form_id=value.get('form_id'),
                        form_type=value.get('form_type'),
                        last_opened_at=value.get('last_opened_at'),
                        last_opened_from_browser=value.get('last_opened_from_browser'),
                        last_opened_from_location=value.get('last_opened_from_location'),
                        last_opened_from_location_city=value.get('last_opened_from_location_city',None),
                        last_opened_from_location_region=value.get('last_opened_from_location_region'),
                        last_opened_from_location_country=value.get('last_opened_from_location_country'),
                        is_form_completed=value.get('is_form_completed'),
                        form_completed_at=value.get('form_completed_at'),
                        last_touched_question_id=value.get('last_touched_question_id'))
                        for value in values
                    ]
            models.ActivityStream.objects.bulk_create(instances)
    except Exception as e:
        print("== Import Exceptions ==\t\t:", str(e))


def import_answers(api_request_url,api_request_header_id,api_request_header_password):
    try:
        # Set API Request header
        headers = {
            'interface-id': api_request_header_id,
            'interface-password': api_request_header_password
        }
        json_response = requests.get(api_request_url, headers=headers).content
        json_response =json.loads(json_response)

        #  Iterate over objects keys and values pairs
        for obj in json_response.items():
            for element in obj:
                if isinstance(element, dict):
                    check_dict(element)

    except Exception as e:
        print("== Import Exceptions ==\t\t:", str(e))


def print_data(value):
    for li in value:
        print(li.get('question_id'))


def check_list(form):
    form_instance = []
    question_instance = []
    for keys in form:
        form_instance = [
            models.Answer(
                result_forms_id=keys.get('id'),
                results_form_default_language=keys.get('form_default_language'),
                results_ip_address=keys.get('ip_address'),
                results_forms_cloned_from=keys.get('cloned_from'),
                results_forms_submitted_at=keys.get('submitted_at'),
            )
        ]

        questions_list = keys.get('questions')
        for question in questions_list:
            question_instance = [
                models.Answer(
                    results_questions_no_answer=question.get('no_answer'),
                    results_questions_field_to_submit_on_ekomi=question.get('field_to_submit_on_ekomi'),
                    results_questions_question_tags=question.get('question_tags'),
                    results_questions_cloned_from=question.get('cloned_from'),
                    results_questions_answer_value=question.get('answer_value'),
                    results_questions_mapped_value=question.get('mapped_value'),

                )
            ]
        models.Answer.objects.bulk_create(form_instance)
        models.Answer.objects.bulk_create(question_instance)

def check_dict(element):
    result_instance = []
    for keys,values in element.items():
        for value in values:
            if isinstance(value, dict):
                result_instance = [
                    models.Answer(
                        result_id=value.get('id'),
                        shop_id=value.get('shop_id'),
                        order_id=value.get('order_id'),
                        product_id=value.get('product_id'),
                        review_hash=value.get('review_hash'),
                        review_status=value.get('review_status'),
                        is_published=value.get('is_published'),
                        published_at=value.get('published_at'),
                        is_withdrawn=value.get('is_withdrawn'),
                        withdrawn_at=value.get('withdrawn_at'),
                    )
                ]
                form=value.get('forms')
                if isinstance(form,list):
                    check_list(form)
    # create bulk operation for final instances group
    models.Answer.objects.bulk_create(result_instance)

 # '''results_questions_answer_value_option_option_id=question.get('id'),
 #                    results_questions_answer_value_option_option_label=question.get('id'),
 #                    results_questions_answer_value_option_linked_questions=question.get('id'),'''