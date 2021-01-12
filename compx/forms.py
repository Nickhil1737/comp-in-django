from django import forms

class UploadFileForm(forms.Form):
    function_name = forms.CharField(max_length=50)
    file = forms.FileField()
#    code = forms.CharField(widget=forms.Textarea)
class texTinpuTforM(forms.Form):
    function_name = forms.CharField(max_length=50)
    code = forms.CharField(widget=forms.Textarea)
