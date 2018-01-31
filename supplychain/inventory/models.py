# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms


from django.db import models
from userregistration.models import User,UserRegistration,UserSignupForm
# Create your models here.
# class CarModel(models.Model):
# 	manufacturerinventory=models.OneToOneField(ManufacturerInventory, on_delete=models.CASCADE, primary_key=True)
# 	model_name=models.CharField()
# 	model_price=models.IntegerField()
# 	numofunits=models.IntegerField()


class ManufacturerInventory(models.Model):
	manufacturerinventory=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	carcount=models.IntegerField()
	#carmodel=models.ForeignKey(CarModel,on_delete=models.CASCADE)

class CarModel(models.Model):
	manufacturerinventory=models.OneToOneField(ManufacturerInventory, on_delete=models.CASCADE, primary_key=True)
	model_name=models.CharField(max_length=15)
	model_price=models.IntegerField()
	numofunits=models.IntegerField()

class CarModelForm(forms.ModelForm):
	class Meta:
		model=CarModel
		fields=['model_name','model_price','numofunits']
	"""docstring for CarModelForm"""
	
		
