# Generated by Django 4.0.2 on 2022-02-21 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0022_alter_title_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['Date']},
        ),
        migrations.AddField(
            model_name='comment',
            name='Date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
