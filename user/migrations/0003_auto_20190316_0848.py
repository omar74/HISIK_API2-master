# Generated by Django 2.1.7 on 2019-03-16 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190316_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='BlockedBy',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='myadmin.Admin'),
        ),
    ]
