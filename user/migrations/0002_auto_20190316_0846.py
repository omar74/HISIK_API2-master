# Generated by Django 2.1.7 on 2019-03-16 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='BlockedBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myadmin.Admin'),
        ),
    ]
