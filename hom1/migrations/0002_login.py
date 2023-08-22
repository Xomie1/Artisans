# Generated by Django 3.2 on 2023-08-16 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hom1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('role', models.CharField(max_length=20)),
            ],
        ),
    ]
