# Generated by Django 3.2.9 on 2022-01-16 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_title_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='post',
        ),
    ]