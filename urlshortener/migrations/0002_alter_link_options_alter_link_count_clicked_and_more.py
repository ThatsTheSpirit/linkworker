# Generated by Django 4.0.4 on 2022-04-23 22:17

import datetime
from django.db import migrations, models
import urlshortener.short_url


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['creation_date', 'expiration_date'], 'verbose_name': 'Ссылка', 'verbose_name_plural': 'Ссылки'},
        ),
        migrations.AlterField(
            model_name='link',
            name='count_clicked',
            field=models.PositiveIntegerField(default=0, verbose_name='Кол-во переходов'),
        ),
        migrations.AlterField(
            model_name='link',
            name='creation_date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='link',
            name='expiration_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата уничтожения'),
        ),
        migrations.AlterField(
            model_name='link',
            name='full_url',
            field=models.URLField(help_text='Source url', max_length=2000, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='link',
            name='short_url',
            field=models.CharField(default=urlshortener.short_url.get_short_url, help_text='Short url', max_length=255, unique=True, verbose_name='Короткая ссылка'),
        ),
    ]