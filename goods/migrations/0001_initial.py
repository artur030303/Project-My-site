# Generated by Django 4.2.7 on 2024-12-14 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категорию',
                'verbose_name_plural': 'Категории',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
                ('mileage', models.PositiveIntegerField(default=0, verbose_name='Пробег (км)')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('full_description', models.TextField(blank=True, null=True, verbose_name='Полное описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='goods_images', verbose_name='Изображение')),
                ('image_slide1', models.ImageField(blank=True, null=True, upload_to='goods_images', verbose_name='Изображение Слайд-1')),
                ('image_slide2', models.ImageField(blank=True, null=True, upload_to='goods_images', verbose_name='Изображение Слайд-2')),
                ('image_slide3', models.ImageField(blank=True, null=True, upload_to='goods_images', verbose_name='Изображение Слайд-3')),
                ('carousel_id', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('price', models.DecimalField(decimal_places=3, default=0.0, max_digits=8, verbose_name='Цена')),
                ('discount', models.DecimalField(decimal_places=3, default=0.0, max_digits=8, verbose_name='Скидка в %')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='goods.categories', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'db_table': 'product',
            },
        ),
    ]
