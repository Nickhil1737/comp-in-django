# Create your views here.
import sys
import csv
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
import importlib
sys.path.append('./compx')

def compHome(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            UploadFileForm.fname = form.cleaned_data['function_name']
            savetofile(request.FILES['file'])
            return HttpResponseRedirect('compxdet')
            
    else:
        form = UploadFileForm()
    return render(request, 'compDetHome.html', {'form': form})

def savetofile(f):
    with open('compx/solve.py', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def compxdet(request):
    from . import newfind
    functionName = UploadFileForm.fname
    filename="solve"
    rescomp = "1"
    lib = importlib.import_module(filename)
    result = getattr(lib,functionName)
    rescomp = newfind.findcompx(result)

    with open('compx/solve.py') as filep:
            pfile =list( csv.reader(filep,delimiter='\n'))

    context = {'functionName':functionName,'pfile':pfile,'rescomp': rescomp}
    return render(request, 'givecomp.html', context)
