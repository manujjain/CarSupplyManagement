# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
#from django.contrib.auth import get_user_model



# Create your models here.
#user=get_user_model()
class ManufacturerManager(models.Manager):
    def get_query_set(self):
        return super(ManufacturerManager, self).get_query_set().filter(type='M')
class DealerManager(models.Manager):
    def get_query_set(self):
        return super(DealerManager, self).get_query_set().filter(type='D')

class CustomerManager(models.Manager):
    def get_query_set(self):
        return super(CustomerManager, self).get_query_set().filter(type='C')

class User(AbstractUser):
    is_manufacturer = models.BooleanField(default=False)
    is_dealer = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    username=models.CharField(unique=True,max_length=30)
    


class UserRegistration(User,models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    #username=models.CharField(max_length=15,unique=True)
    
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    balance = models.IntegerField(null=True)
    USER_TYPE=(
        ('M','Manufacturer'),
        ('D','Dealer'),
        ('C','Customer'),
        )

    type=models.CharField(max_length=1,choices=USER_TYPE,default='Customer')
    manufacturers=ManufacturerManager()
    dealers=DealerManager()
    customers=CustomerManager()


class UserSignupForm(forms.ModelForm):
    class Meta:
        model=UserRegistration
        fields= ['name', 'username','password', 'country', 'balance','type']
        #form=ManufacturerSignupForm()

        # if form.is_valid():
        #     # Check if user is available 
        #     if request.user.is_authenticated():
        #         # Add missing user to model form
        #         form.instance.user = request.user
        #         user.is_manufacturer=True
        #     # Insert into DB
        #     form.save()
  
      