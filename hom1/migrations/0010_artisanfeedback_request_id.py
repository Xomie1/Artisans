# Generated by Django 3.2 on 2023-08-22 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hom1', '0009_artisanfeedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='artisanfeedback',
            name='request_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
