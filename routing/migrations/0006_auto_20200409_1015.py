# Generated by Django 3.0.4 on 2020-04-09 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('routing', '0005_auto_20200409_0938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session',
            old_name='date',
            new_name='delivery_date',
        ),
    ]
