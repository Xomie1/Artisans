# Generated by Django 3.2 on 2023-08-17 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hom1', '0005_remove_login_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='profession',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='role',
            field=models.CharField(choices=[('user', 'User'), ('artisan', 'Artisan')], default='user', max_length=20),
        ),
    ]
