# Generated by Django 2.0.2 on 2018-09-26 13:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenderResponse',
            fields=[
                ('idgender', models.BigAutoField(primary_key=True, serialize=False)),
                ('isEnabled', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=24)),
                ('points', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('idstudent', models.BigAutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=24)),
                ('lastname', models.CharField(max_length=24)),
                ('schoolname', models.CharField(max_length=32)),
                ('aliasname', models.CharField(default='none', max_length=12, unique=True)),
                ('aliaspin', models.CharField(default='none', max_length=4)),
                ('shortssn', models.CharField(default='none', max_length=4)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('parentfirstname', models.CharField(max_length=24)),
                ('parentlastname', models.CharField(max_length=24)),
                ('telephone', models.CharField(blank=True, default='7045550000', max_length=10, validators=[django.core.validators.RegexValidator(message='Area code and number', regex='^\\d{3}-\\d{3}-\\d{4}$|^\\d{10}$|^\\d{3} \\d{3} \\d{4}$')])),
                ('email', models.CharField(blank=True, default='you@somewhere.com', max_length=32, validators=[django.core.validators.RegexValidator(message='name@domain.com', regex='^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$')])),
                ('streetAddress', models.CharField(blank=True, max_length=32)),
                ('city', models.CharField(blank=True, max_length=16)),
                ('state', localflavor.us.models.USStateField(blank=True, max_length=2)),
                ('zip', localflavor.us.models.USZipCodeField(blank=True, max_length=10)),
                ('timelineStartDate', models.DateField(blank=True, null=True)),
                ('gender', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='iccdbook.GenderResponse')),
            ],
        ),
    ]