# Generated by Django 2.2.3 on 2019-08-07 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paste', '0005_paste_die_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paste',
            name='life_time',
            field=models.CharField(choices=[('10 MIN', '10 min')], max_length=10),
        ),
    ]
