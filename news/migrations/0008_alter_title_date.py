# Generated by Django 3.2.9 on 2022-01-26 18:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_title_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 26, 19, 26, 1, 667202)),
        ),
    ]