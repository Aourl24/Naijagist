# Generated by Django 3.2.9 on 2022-01-31 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_alter_title_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='title',
            options={},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='Part',
        ),
    ]
