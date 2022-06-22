# Generated by Django 3.2.9 on 2022-01-23 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='title',
            name='category',
            field=models.CharField(max_length=30),
        ),
    ]
