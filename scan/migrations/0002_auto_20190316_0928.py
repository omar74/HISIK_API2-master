# Generated by Django 2.1.7 on 2019-03-16 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scan',
            name='Category',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='category.Category'),
        ),
        migrations.AlterField(
            model_name='scan',
            name='brand',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='brand.Brand'),
        ),
        migrations.AlterField(
            model_name='scan',
            name='product',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product'),
        ),
    ]
