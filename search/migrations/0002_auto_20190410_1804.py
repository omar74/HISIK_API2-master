# Generated by Django 2.1.7 on 2019-04-10 16:04

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='search',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
