from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    employee_first_name = forms.CharField(max_length=30, required=True,)
    employee_last_name = forms.CharField(max_length=30, required=True,)
   
    
    email = forms.EmailField(max_length=254, help_text='Required. A valid email address.')

    class Meta:
        model = User
        fields = ('username', 'employee_first_name',"employee_last_name", 'email' )

class ChangePasswordForm(forms.Form):
    attrs = {
        "type": "password"
    }
    current_password = forms.CharField(widget=forms.TextInput(attrs=attrs))
    new_password = forms.CharField(widget=forms.TextInput(attrs=attrs))
    new_password_again = forms.CharField(widget=forms.TextInput(attrs=attrs))

    

