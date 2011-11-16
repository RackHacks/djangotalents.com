from django import forms

ACCOUNT_CHOICES = (
    (1, 'Player'),
    (2, 'Clinic'),
    (3, 'Coach'),
    (4, 'Court owner'),
)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)