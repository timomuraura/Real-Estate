# Generated by Django 4.2.18 on 2025-01-21 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='usertype',
            field=models.CharField(choices=[('admin', 'Admin'), ('user', 'User')], max_length=10),
        ),
    ]
