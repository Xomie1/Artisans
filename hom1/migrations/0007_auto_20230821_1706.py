# Generated by Django 3.2 on 2023-08-21 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hom1', '0006_auto_20230817_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='artisan_name',
        ),
        migrations.AddField(
            model_name='feedback',
            name='request',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hom1.request'),
            preserve_default=False,
        ),
    ]
