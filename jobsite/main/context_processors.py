from django.contrib.auth.forms import AuthenticationForm

def login_form(request):
    auth_form = AuthenticationForm()
    if request.method == 'POST':
        auth_form = AuthenticationForm(None, request.POST)
    return {
        'login_form': auth_form
    }