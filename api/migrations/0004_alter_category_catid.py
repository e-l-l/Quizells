# Generated by Django 4.1 on 2022-08-07 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_category_catid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='catid',
            field=models.CharField(default='newcat', max_length=50),
        ),
    ]