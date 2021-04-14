from django.db import models


# Create your models here.


class Form(models.Model):
    form_id = models.IntegerField(default=False, null=True, blank=True)
    name = models.CharField(max_length=50, default=False, null=True, blank=True)
    type = models.CharField(max_length=50, default=False, null=True, blank=True)
    completion_rate = models.IntegerField(default=False, null=True, blank=True)
    open_rate = models.IntegerField(default=False, null=True, blank=True)
    is_default = models.IntegerField(default=False, null=True, blank=True)
    is_default_form_of_default_survey = models.IntegerField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name


class Account(models.Model):
    form_key = models.ForeignKey(Form, on_delete=models.CASCADE, default=True, null=True, blank=True, )
    account_id = models.CharField(max_length=50, default=False, null=True, blank=True)
    account_name = models.CharField(max_length=50, default=False, null=True, blank=True)
    account_password = models.CharField(max_length=50, default=False, null=True, blank=True)

    def __str__(self):
        return self.account_name


class Question(models.Model):
    form_key = models.ForeignKey(Form, on_delete=models.CASCADE, default=True, null=True, blank=True)
    question_id = models.IntegerField(default=False, null=True, blank=True)
    question_label = models.CharField(max_length=100, default=False, null=True, blank=True)
    question_type = models.CharField(max_length=10, null=True, blank=True)
    parent_id = models.IntegerField(default=False, null=True, blank=True)
    is_conditional_question = models.BooleanField(default=False, null=True, blank=True)
    is_required = models.BooleanField(default=False, null=True, blank=True)
    status = models.CharField(max_length=10, default=False, null=True, blank=True)
    min_range = models.IntegerField(default=False, null=True, blank=True)
    max_range = models.IntegerField(default=False, null=True, blank=True)


class Answer(models.Model):
    question_key = models.ForeignKey(Question, on_delete=models.CASCADE, default=2, null=True, blank=True)
    result_id = models.IntegerField(default=False, null=True, blank=True)
    shop_id = models.IntegerField(default=False, null=True, blank=True)
    order_id = models.CharField(max_length=100, default=False, null=True, blank=True)
    product_id = models.CharField(max_length=100, default=False, null=True, blank=True)
    review_hash = models.CharField(max_length=100, default=False, null=True, blank=True)
    review_status = models.CharField(max_length=100, default=False, null=True, blank=True)
    is_published = models.BooleanField(null=True, blank=True)
    published_at = models.BooleanField(null=True, blank=True)
    is_withdrawn = models.CharField(max_length=100, default=False, null=True, blank=True)
    withdrawn_at = models.CharField(max_length=100, default=False, null=True, blank=True)
    result_forms_id = models.IntegerField(default=False, null=True, blank=True)
    results_form_default_language = models.CharField(max_length=100, default=False, null=True, blank=True)
    results_ip_address = models.CharField(max_length=100, default=False, null=True, blank=True)
    results_forms_cloned_from = models.IntegerField(default=False, null=True, blank=True)
    results_forms_submitted_at = models.IntegerField(default=False, null=True, blank=True)
    results_questions_no_answer = models.IntegerField(default=False, null=True, blank=True)
    results_questions_field_to_submit_on_ekomi = models.BooleanField(null=True, blank=True)
    results_questions_question_tags = models.CharField(max_length=100, default=False, null=True, blank=True)
    results_questions_cloned_from = models.IntegerField(default=False, null=True, blank=True)
    results_questions_answer_value = models.CharField(max_length=100, default=False, null=True, blank=True)
    results_questions_answer_value_option_option_id = models.CharField(max_length=100, default=False, null=True, blank=True)
    results_questions_answer_value_option_option_label = models.CharField(max_length=100, default=False, null=True, blank=True)
    results_questions_answer_value_option_linked_questions = models.CharField(max_length=100, default=False, null=True, blank=True)
    results_questions_mapped_value = models.IntegerField(default=False, null=True, blank=True)


class ActivityStream(models.Model):
    form_key = models.ForeignKey(Form, on_delete=models.CASCADE, default=True, null=True, blank=True)
    order_id = models.CharField(max_length=50, default=False, null=True, blank=True)
    form_id = models.IntegerField(default=False, null=True, blank=True)
    form_type = models.CharField(max_length=50, default=False, null=True, blank=True)
    last_opened_at = models.CharField(max_length=50, default=False, null=True, blank=True)
    last_opened_from_browser = models.CharField(max_length=50, default=False, null=True, blank=True)
    last_opened_from_location = models.CharField(max_length=50, default=False, null=True, blank=True)
    last_opened_from_location_city = models.CharField(max_length=50, default=False, null=True, blank=True)
    last_opened_from_location_region = models.CharField(max_length=50, default=False, null=True, blank=True)
    last_opened_from_location_country = models.CharField(max_length=50, default=False, null=True, blank=True)
    is_form_completed = models.BooleanField(default=False, null=True, blank=True)
    form_completed_at = models.CharField(max_length=50, default=False, null=True, blank=True)
    last_touched_question_id = models.IntegerField(default=False, null=True, blank=True)

