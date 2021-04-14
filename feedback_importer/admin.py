from django.contrib import admin
from .models import Form, Account, Question, ActivityStream, Answer
from django.core.serializers.json import DjangoJSONEncoder

admin.site.site_header = "Smart Feedback"
admin.site.site_title = "Smart Feedback"
admin.site.index_title = "Smart Feedback"


class FormAdmin(admin.ModelAdmin):
    list_display = ('id', 'form_id', "name", "type", "completion_rate", "open_rate", "is_default", "is_default_form_of_default_survey")
    list_max_show_all = 25
    ordering = ['pk']
    list_filter = ("name",)


admin.site.register(Form, FormAdmin)
# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'form_key', "account_id", "account_name", "account_password")
    list_max_show_all = 25
    ordering = ['pk']
    list_filter = ("account_name",)


admin.site.register(Account, AccountAdmin)
# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'form_key', "question_id", "question_label", "question_type", "parent_id", "is_conditional_question", "is_required", "status", "min_range", "max_range")
    list_max_show_all = 25
    ordering = ['pk']

admin.site.register(Question, QuestionAdmin)
# Register your models here.


class ActivityStreamAdmin(admin.ModelAdmin):
    list_display = ('id', 'form_key', "form_id", "form_type", "last_opened_at", "last_opened_from_browser", "last_opened_from_location", "last_opened_from_location_city", "last_opened_from_location_region", "last_opened_from_location_country", "is_form_completed", "form_completed_at", "last_touched_question_id")
    list_max_show_all = 25
    ordering = ['pk']


admin.site.register(ActivityStream, ActivityStreamAdmin)
# Register your models here.


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_key', "result_id", "shop_id", "order_id", "product_id", "review_hash", "review_status", "is_published", "published_at", "is_withdrawn", "withdrawn_at", "result_forms_id", "results_form_default_language", "results_ip_address", "results_forms_cloned_from", "results_forms_submitted_at", "results_questions_no_answer", "results_questions_field_to_submit_on_ekomi", "results_questions_question_tags", "results_questions_cloned_from", "results_questions_answer_value", "results_questions_answer_value_option_option_id", "results_questions_answer_value_option_option_label", "results_questions_answer_value_option_linked_questions", "results_questions_mapped_value")
    list_max_show_all = 25
    list_display_links = ('question_key', 'id')
    ordering = ['pk']


admin.site.register(Answer, AnswerAdmin)
# Register your models here.
