# Generated by Django 3.2 on 2021-04-12 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback_importer', '0004_auto_20210411_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitystream',
            name='form_type',
            field=models.CharField(blank=True, default=False, max_length=50, null=True),
        ),
    ]
