# Generated by Django 2.2.6 on 2019-11-04 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EMS', '0013_request_enc_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='paper',
        ),
    ]
