# Generated by Django 2.0.2 on 2018-09-26 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iccdbook', '0005_auto_20180926_0952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='gender',
        ),
        migrations.DeleteModel(
            name='GenderResponse',
        ),
    ]