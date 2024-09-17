from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=256)
    phone = models.CharField(max_length=13)  #PhoneNumberField()
    email = models.EmailField()
    tgid = models.IntegerField()
    myrole = models.CharField(choices={'a': 'manager', 'm': 'master', 'c': 'client'})
