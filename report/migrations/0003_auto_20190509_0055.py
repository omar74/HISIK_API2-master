# Generated by Django 2.1.7 on 2019-05-08 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_auto_20190410_1804'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='proudct',
            new_name='product',
        ),
    ]
