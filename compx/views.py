# Create your views here.
from django.views.generic import TemplateView
import sys
from django.http import HttpResponseRedirect
#from django.views import View
from django.urls import reverse
from django.views.generic.base import TemplateView

from django.shortcuts import render
from .forms import UploadFileForm
from .models import ModelWithFileField
import importlib
sys.path.append('./compx')

class homepage(TemplateView):
    template_name = 'index.html'

class MyFormView(TemplateView):
    form_class = UploadFileForm
    template_name = 'compDetHome.html'
    model = ModelWithFileField

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        instances = ModelWithFileField.objects.all()
        return render(request, self.template_name, {'form':form,'instances':instances})

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
            timetakenlist,rescomp = newfind.findcompx(result)
            print(timetakenlist)
            pfile = ""

            with open('compx/solve.py') as filep:
                pfile=filep.readlines()


            instance = ModelWithFileField(fname_field=fname,code_field=pfile,complexity_field=rescomp,complexity_key=rescomp,time1_field=str(timetakenlist[0]),time2_field=str(timetakenlist[1]),time3_field=str(timetakenlist[2]))
            instance.save()
            # <process form cleaned data>
            return HttpResponseRedirect(reverse('compxdet',kwargs={'pk':instance.id}))

        return render(request, self.template_name,{'form': form,})

class compxdet(TemplateView):
    template_name = 'givecomp.html'
    model = ModelWithFileField
    def get(self, request, *args, **kwargs):
        instances = ModelWithFileField.objects.get(id=kwargs['pk'])
        return render(request, self.template_name, {'instances':instances})
def savetofile(f):
    with open('compx/solve.py', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
