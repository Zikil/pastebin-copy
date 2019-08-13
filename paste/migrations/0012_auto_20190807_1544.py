# Generated by Django 2.2.3 on 2019-08-07 15:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paste', '0011_auto_20190807_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paste',
            name='life_time',
            field=models.DateTimeField(choices=[(datetime.timedelta(0, 60), '1 min'), (datetime.timedelta(0, 600), '10 min'), (datetime.timedelta(0, 3600), '1 hour'), (datetime.timedelta(1), '1 day'), (datetime.timedelta(7), '1 week'), (datetime.timedelta(30), '1 month'), (datetime.timedelta(365), '1 year'), (datetime.timedelta(0), 'inf')], default=datetime.timedelta(0), max_length=4),
        ),
    ]
