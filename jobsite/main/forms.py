from django import forms
from django.forms import Select
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from main.country_choices import COUNTRIES as COUNTRY_CHOICES
from main.models import UserProfile

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea, max_length=1000)

class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        del self.fields['username']

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

class SignupForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('country',)
        widgets = {
            'country': Select(choices=COUNTRY_CHOICES)
        }
