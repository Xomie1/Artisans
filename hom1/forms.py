from django import forms
from hom1.models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email', 'password','role', 'address', 'phone_number', 'profession' ]
        widgets = {
            'password': forms.PasswordInput(),
        }
