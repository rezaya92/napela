# Generated by Django 3.1.3 on 2020-11-09 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookAdvertisement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookad',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
