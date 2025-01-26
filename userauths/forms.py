from django import forms
from django.contrib.auth.forms import UserCreationForm


from userauths.models import User

USER_TYPE=(
    ('Vendor', 'Vendor'),
    ('Customer', 'Customer')
)

class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded','placeholder':'Enter '
                                                                                                           'Fullname'}),required=True)
    mobile = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded', 'placeholder':'Enter Mobile'}), required=True)
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded','placeholder':'Enter Email '
                                                                                              'Address'}),required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control rounded','placeholder':'Enter Password'}),required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control rounded','placeholder':'Repeat Password'}),required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE,widget=forms.Select(attrs={'class':'form-select'}))


    class Meta:
        model=User
        fields=['full_name','mobile','email','password1','password2','user_type']

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded', 'placeholder':'Enter Email'}),
                            required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control rounded',
                                                                 'placeholder':'Enter Password'}), required=True)

    class Meta:
        model=User
        fields=['email', 'password']




















