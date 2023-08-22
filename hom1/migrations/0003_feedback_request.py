# Generated by Django 3.2 on 2023-08-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hom1', '0002_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artisan_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('feedback', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artisan_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
    ]