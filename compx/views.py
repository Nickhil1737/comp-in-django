# Create your views here.
import sys
import csv
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import UploadFileForm
from .models import ModelWithFileField
import importlib
sys.path.append('./compx')

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

def savetofile(f):
    with open('compx/solve.py', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def compxdet(request):
    instance1 = ModelWithFileField.objects.get(pk=12)
    context = {}
    context['instance1'] = instance1
    return render(request, 'givecomp.html', context)
