# Generated by Django 2.0.2 on 2018-09-26 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iccdbook', '0002_auto_20180926_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='aliasname',
            field=models.CharField(default='none', max_length=12, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='aliaspin',
            field=models.CharField(default='none', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='parentfirstname',
            field=models.CharField(max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='parentlastname',
            field=models.CharField(max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='shortssn',
            field=models.CharField(default='none', max_length=4, null=True),
        ),
    ]