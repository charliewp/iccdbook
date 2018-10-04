from django.db import models

from datetime import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import RegexValidator
from django.contrib.contenttypes.models import ContentType

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


from localflavor.us.models import USStateField
from localflavor.us.models import USZipCodeField

# Create your models here.
class Status(models.Model):
    idstatus = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=24)
    def __str__(self):
        return self.name
        
class Student(models.Model):
    idstudent = models.BigAutoField(primary_key=True)
    firstname = models.CharField(max_length=24)
    lastname = models.CharField(max_length=24)
    schoolname = models.CharField(null=True, max_length=32)
    aliasname = models.CharField(null=True, max_length=12, unique=True, default='none')
    aliaspin = models.CharField(null=True, max_length=4, default='none')
    shortssn = models.CharField(null=True, max_length=4, default='none')
    birthdate = models.DateField(null=True, blank=True)
    parentfirstname = models.CharField(null=True,max_length=24)
    parentlastname = models.CharField(null=True,max_length=24)
    phone_regex = RegexValidator(regex=r'^\d{3}-\d{3}-\d{4}$|^\d{10}$|^\d{3} \d{3} \d{4}$', message='Area code and number')
    telephone = models.CharField(null=True, validators=[phone_regex], max_length=10, blank=True, default='7045550000')
    email_regex = RegexValidator(regex=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', message='name@domain.com')
    email = models.CharField(null=True,validators=[email_regex], max_length=32, blank=True, default='you@somewhere.com')
    streetAddress = models.CharField(null=True, max_length=32,blank=True)
    city = models.CharField(null=True, max_length=16,blank=True)
    state = USStateField(null=True, blank=True)
    zip = USZipCodeField(null=True, blank=True)
    timelineStartDate = models.DateField(null=True, blank=True)
    status = models.IntegerField(null=True, default=0)
    nfccardid = models.IntegerField(null=True, default=0)
    
