# Generated by Django 5.1.4 on 2025-01-03 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_alter_products_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='carousel_id',
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
    ]
