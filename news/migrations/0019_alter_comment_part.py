# Generated by Django 3.2.9 on 2022-02-06 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0018_alter_title_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Part',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='news.title'),
            preserve_default=False,
        ),
    ]