# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
# Create your views here.
from userregistration.models import UserRegistration
from .models import CarModel, ManufacturerInventory,CarModelForm

# class Carcreation(CreateView):
#     model = CarModel
#     form_class = CarModelForm
#     success_url = reverse_lazy('manufacturer:success')
#     template_name = "carmodelform.html"
#     form=CarModelForm()
#     def form_valid(self, form):
#         obj = form.save(commit=False)
#         model_name=form.cleaned_data.get("model_name")
#         model_price=form.cleaned_data.get('model_price')
#         numofunits=form.cleaned_data.get('numofunits')
        
        
#         obj.save()
#         return redirect('manufacturer:success')
#     def __init__(self,form):
#     	model_name=self.cleaned_data.get("model_name")
#         model_price=self.cleaned_data.get('model_price')
#         numofunits=self.cleaned_data.get('numofunits')
#         context = Context({
#         'model_name': model_name,
#         'model_price': model_price,
#         })
#         return render(request,'home.html',{'model_name': model_name,'model_price': model_price})
#     def carmodelname(self):
#     	return CarModel.objects.all()
    
#     def get_context_data(self, **kwargs):
#         context = super(Carcreation, self).get_context_data(**kwargs)
#         context['carmodelname'] = CarModel.model_name
#         return context
# # 
def carcreation(request):
    form = CarModelForm(request.POST or None)
    context={"form":form}
    print("User Logged in")
    print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        obj=form.save(commit=False)
        model_name=form.cleaned_data.get("model_name")
        model_price=form.cleaned_data.get('model_price')
        numofunits=form.cleaned_data.get('numofunits')
        obj.save()
        oik=UserRegistration.objects.all()
        return render(request,"home.html",{'obj':obj,'oik':oik})

        
        # user = authenticate(request, username=username, password=password)
        # if user.is_authenticated:
          
        #if user is not None:
         #  print(request.user.is_authenticated())
          
        # Redirect to a success page.
           
    else:
        pass


    return render(request,"carmodelform.html",context)

