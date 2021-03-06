# Generated by Django 2.2.3 on 2019-07-28 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=8, unique=True)),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('body', models.TextField(db_index=True)),
                ('author', models.CharField(db_index=True, max_length=150)),
                ('life_time', models.IntegerField()),
                ('die_time', models.DateTimeField(blank=True)),
                ('access', models.CharField(max_length=50)),
            ],
        ),
    ]
