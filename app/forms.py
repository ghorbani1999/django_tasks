from django import forms
from .models import tasks , person
class taskform(forms.ModelForm):
    class Meta :
        model = tasks
        fields = ['title' , 'description']
class personform(forms.ModelForm):
    class Meta :
        model = person
        fields = ['name' , 'sex']