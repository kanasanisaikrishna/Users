# Generated by Django 4.2.4 on 2024-04-12 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='subject',
        ),
    ]
