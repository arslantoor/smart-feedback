# Generated by Django 3.2 on 2021-04-14 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback_importer', '0016_auto_20210414_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='is_withdrawn',
            field=models.CharField(blank=True, default=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='withdrawn_at',
            field=models.CharField(blank=True, default=False, max_length=100, null=True),
        ),
    ]
