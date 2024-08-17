# Generated by Django 5.1 on 2024-08-15 18:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_alter_historybook_data_of_capture_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historybook',
            name='aaa',
        ),
        migrations.AlterField(
            model_name='historybook',
            name='data_of_capture',
            field=models.CharField(default=datetime.datetime(2024, 8, 15, 21, 13, 5, 471604), max_length=20, verbose_name='Дата выдачи'),
        ),
        migrations.AlterField(
            model_name='historybook',
            name='data_of_return',
            field=models.CharField(default=datetime.datetime(2024, 8, 15, 21, 13, 5, 471604), max_length=20, verbose_name='Дата возврата'),
        ),
    ]
