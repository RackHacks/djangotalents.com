from django import forms
from django.forms import Select
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField
from main.models import UserProfile


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea, max_length=1000)
    captcha = CaptchaField()

    def send(self, recipient='djangotalents@codenga.com'):
        return send_mail(
            self.cleaned_data['subject'],
            self.cleaned_data['message'],
            self.cleaned_data['sender'],
            [recipient],
        )

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class SignupForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = UserProfile
        fields = ('country', 'captcha',)

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)