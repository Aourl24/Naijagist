# Generated by Django 3.2.9 on 2022-01-31 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_title_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ['-Date']},
        ),
    ]
