# Generated by Django 5.1 on 2024-08-20 08:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0003_schoolclass'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schoolclass',
            options={'verbose_name': 'Классы', 'verbose_name_plural': 'Классы'},
        ),
        migrations.AlterField(
            model_name='reader',
            name='school_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reader.schoolclass', verbose_name='Класс'),
        ),
    ]