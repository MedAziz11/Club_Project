from django.contrib.auth.models import User
from django import forms
from .models import Profile


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=15,required=True, widget=forms.TextInput(
        attrs={'placeholder' : "Club Name"}
    ))
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'placeholder' : "Email"}
    ) )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder' : "Password" , "id":"password", "name":"password"}
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder' : "Re_Password", "id":"password1", "name":"password1"}
    ))

    class Meta:
        model = User
        fields = ("username",  "email", "password" ,)


    def clean_username(self, *args, **kwargs): # Validates the Username Field
        username = self.cleaned_data.get('username')
        queryset = User.objects.filter(username=username)
        if len(queryset)>0:
            raise forms.ValidationError(username + ' is already used')
        return username

    def clean_email(self, *args):
        email = self.cleaned_data.get('email')
        queryset = User.objects.filter(email=email)
        if len(queryset)>0:
            raise forms.ValidationError('email is already used')
        return email

    def clean_password1(self, *args):
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')
        if password and password1 and password==password1 :
            return password
        else:
            raise forms.ValidationError('password doesnt match')

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ("image",)



      

