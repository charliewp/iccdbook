# Generated by Django 2.0.2 on 2018-09-26 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iccdbook', '0003_auto_20180926_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='schoolname',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
