# Generated by Django 3.1.4 on 2020-12-22 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20201222_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='entrance_year',
            field=models.IntegerField(verbose_name='entrance year'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='field',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='field'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='phone number'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='university',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='university'),
        ),
    ]
