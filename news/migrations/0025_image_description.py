# Generated by Django 4.0.2 on 2022-06-16 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0024_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]