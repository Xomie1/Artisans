# Generated by Django 3.2 on 2023-08-17 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hom1', '0003_feedback_request'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='user_id',
        ),
    ]