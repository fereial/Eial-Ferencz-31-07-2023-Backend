# Generated by Django 3.2 on 2023-08-02 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='api_user',
        ),
    ]
