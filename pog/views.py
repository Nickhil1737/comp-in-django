import sys
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from . import newfind

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('pogsolve')
            
    else:
        form = UploadFileForm()
    return render(request, 'upload_doc.html', {'form': form})

def handle_uploaded_file(f):
    with open('pog/solve.py', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def pogsolve(request):
    rescomp = newfind.findcompx()
    filep = open("pog/solve.py","r")
    pfile = filep.readlines()

    context = {'pfile':pfile,'rescomp': rescomp}
    return render(request, 'givecomp.html', context)
