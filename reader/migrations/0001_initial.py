# Generated by Django 5.1 on 2024-08-11 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('school_class', models.CharField(choices=[('1А', '1А'), ('1Б', '1Б'), ('1В', '1В'), ('2А', '2А'), ('2Б', '2Б'), ('2В', '2В'), ('3А', '3А'), ('3Б', '3Б'), ('3В', '3В'), ('4А', '4А'), ('4Б', '4Б'), ('4В', '4В'), ('5А', '5А'), ('5Б', '5Б'), ('5В', '5В'), ('6А', '6А'), ('6Б', '6Б'), ('6В', '6В'), ('7А', '7А'), ('7Б', '7Б'), ('7В', '7В'), ('8А', '8А'), ('8Б', '8Б'), ('8В', '8В'), ('9А', '9А'), ('9Б', '9Б'), ('9В', '9В'), ('10А', '10А'), ('10Б', '10Б'), ('11А', '11А')], max_length=3)),
            ],
            options={
                'verbose_name': 'Ученики',
                'verbose_name_plural': 'Ученики',
            },
        ),
    ]
