# Generated by Django 3.1.3 on 2020-11-23 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='feature',
            field=models.BooleanField(null=True),
        ),
    ]
