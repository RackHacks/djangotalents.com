from django.contrib.auth.models import User
from countries.models import Country
from main.models import UserProfile


def create_user(username='johnlenon', email='john@thebeatles.com',
                password='johnLenon123', active=True):
    kwargs = {
        'username': username,
        'email': email,
        'password': password,
    }
    new_user = User.objects.create_user(**kwargs)
    new_user.is_staff = False
    new_user.is_active = active
    new_user.save()
    country = Country.objects.get(iso='MX')
    profile = UserProfile.objects.create(user=new_user, country=country)
    return new_user
