from django import forms
from .models import User_Details
class UserForm(forms.ModelForm):
    class Meta:
        model = User_Details
        fields = ['id','username','email','password']