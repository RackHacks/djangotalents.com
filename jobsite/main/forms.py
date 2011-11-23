from django import forms
from django.forms import Select
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField
from main.models import UserProfile


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea, max_length=1000)

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class SignupForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = UserProfile
        fields = ('country', 'captcha',)
