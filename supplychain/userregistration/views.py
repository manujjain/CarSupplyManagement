# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User,UserRegistration,UserSignupForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from inventory.views import carcreation

from inventory.models import CarModel


def home(request):
    # obj=UserRegistration.objects.all()
    # oij=UserRegistration.objects.all()
    
    oik=UserRegistration.objects.all()
    return render(request,'home.html',{'oik':oik})
class Usercreation(CreateView):
    model = UserRegistration
    form_class = UserSignupForm
    success_url = reverse_lazy('manufacturer:success')
    template_name = "ManufacturerSignupForm.html"
    form=UserSignupForm()
    def form_valid(self, form):
        obj = form.save(commit=False)
        password=form.cleaned_data.get("password")
        obj.set_password(password)
        obj.save()
        
        return redirect('manufacturer:success')
    # def carmodelname(self):
    #     return CarModel.objects.all()
    # def get_context_data(self, **kwargs):
    #     context = super(carcreation, self).get_context_data(**kwargs)
    #     context['carmodelname'] = CarModel.model_name
    #     return context
    
    # if form.is_valid():
    #          userobj=form.cleaned_data
    #          username=userobj['username']
    #          name=userobj['name']
    #          password=userobj['password']
    #          User.objects.create_user(username,name,password)
    #          user=authenticate(username=username,password=password)
             # print(form.cleaned_data)
             # print("User Logged in")
             # print(request.user.is_authenticated())

            # Check if user is available 
             #if request.user.is_authenticated():
                #login(request, user)
                # Add missing user to model form
                #form.instance.user = request.user

               # username=form.cleaned_data.get("username")

        		#password=form.cleaned_data.get("password")

                
            # Insert into DB
             #form.save()
             #user.save()
            #user=form.save()

            #print(user.name)

  


def get_query(request):
	def get_queryset(self,*args,**kwargs):
	    obj=UserRegistration.objects.all()
	return render(request,'object.html',{'obj':'obj'})
def login_page(request):
    form = LoginForm(request.POST or None)
    context={"form":form}
    print("User Logged in")
    print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        
        username = request.POST['username']
        password = request.POST['password']
        
        
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
           print(request.user.is_authenticated())
           obj=UserRegistration.objects.filter(username=username)
           for item in obj:
            user_name=item.name
            user_country=item.country
            user_balance=item.balance
           
        #if user is not None:
         #  print(request.user.is_authenticated())
           print(user_name)
           login(request,user)
        # Redirect to a success page.
           return render(request,'home.html',{'names':user_name,'country':user_country,'balance':user_balance})
        else:
           return redirect("/home/")
        #
        #else:
        # Return an 'invalid login' error message.
           #print("There are some issues")
        #
        #context["form"]=LoginForm()

    return render(request,"loginform.html",context)
