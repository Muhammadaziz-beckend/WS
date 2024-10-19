# Generated by Django 5.1 on 2024-10-19 03:16

import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_apartment_user_city_user_displayname_user_floor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='apartment',
            field=models.CharField(max_length=10, verbose_name='квартира'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='WEBP', keep_meta=True, quality=90, scale=None, size=[500, 500], upload_to='avatars/', verbose_name='аватарка'),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=100, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='user',
            name='displayname',
            field=models.CharField(max_length=255, verbose_name='Отображаемое имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='floor',
            field=models.CharField(max_length=10, verbose_name='Этаж'),
        ),
        migrations.AlterField(
            model_name='user',
            name='house',
            field=models.CharField(max_length=10, verbose_name='Дом'),
        ),
        migrations.AlterField(
            model_name='user',
            name='street',
            field=models.CharField(max_length=100, verbose_name='Улица'),
        ),
    ]
