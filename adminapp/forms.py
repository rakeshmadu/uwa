from .models import Reg
from django import forms


class Sigupform(forms.ModelForm):
    class Meta:
            model = Reg
            fields = "__all__"
            widgets = {
            'password': forms.PasswordInput(),
        } 

class Signinform(forms.ModelForm):
    class Meta:
        model = Reg
        fields = ['Email','password']    
        widgets = {
            'password': forms.PasswordInput(),
        }    




