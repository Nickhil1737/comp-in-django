# Create your views here.
from django.views.generic import TemplateView
import sys
import csv
from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render
from .forms import UploadFileForm
from .models import ModelWithFileField
import importlib
sys.path.append('./compx')




class MyFormView(View):
    form_class = UploadFileForm
    initial = {'key': 'value'}
    template_name = 'compDetHome.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            fname = form.cleaned_data['function_name']
            savetofile(request.FILES['file'])
            from . import newfind
            filename="solve"
            rescomp = "1"
            lib = importlib.import_module(filename)
            result = getattr(lib,fname)
            rescomp = newfind.findcompx(result)
            pfile = ""

            with open('compx/solve.py') as filep:
                pfile=filep.readlines()


            instance = ModelWithFileField(fname_field=fname,code_field=pfile,complexity_field=rescomp)
            instance.save()
            # <process form cleaned data>
            return HttpResponseRedirect('compxdet')

        return render(request, self.template_name,{'form': form,'allinstances':ModelWithFileField.objects.all()})
"""
def compHome(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fname = form.cleaned_data['function_name']
            savetofile(request.FILES['file'])
            from . import newfind
            filename="solve"
            rescomp = "1"
            lib = importlib.import_module(filename)
            result = getattr(lib,fname)
            rescomp = newfind.findcompx(result)
            pfile = ""

            with open('compx/solve.py') as filep:
                pfile=filep.readlines()


            instance = ModelWithFileField(fname_field=fname,code_field=pfile,complexity_field=rescomp)
            instance.save()
            return HttpResponseRedirect(reverse('compxdet'))
            
    else:
        form = UploadFileForm()
    return render(request, 'compDetHome.html', {'form': form,'allinstances':ModelWithFileField.objects.all()})
"""
def savetofile(f):
    with open('compx/solve.py', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def compxdet(request):
    instances = ModelWithFileField.objects.all()
    context = {}
    context['instances'] = instances
    return render(request, 'givecomp.html', context)
