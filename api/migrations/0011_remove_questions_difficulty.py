# Generated by Django 4.1 on 2022-08-07 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_rename_qid_quizzes_quizid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='difficulty',
        ),
    ]