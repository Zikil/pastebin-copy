# Generated by Django 2.2.3 on 2019-08-07 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paste', '0006_auto_20190807_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paste',
            name='life_time',
            field=models.IntegerField(choices=[('100', '10 min'), ('200', '20 min')], max_length=10),
        ),
    ]
