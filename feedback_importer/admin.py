from django.contrib import admin
from .models import Test,Form,Account,Question,ActivityStream
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
    list_display = ('id', 'form_key', "name", "type")
    list_max_show_all = 25
    ordering = ['pk']
    list_filter = ("name",)


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


class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'field_1', "field_2", "field_3")
    list_max_show_all = 25
    ordering = ['pk']


admin.site.register(Test, TestAdmin)
# Register your models here.
