# -.- coding: utf8 -.-
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client
from sure import that
from captcha.models import CaptchaStore
from jobsite.lib.test_helpers import create_user
from main.models import UserProfile


class AuthTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = '/accounts/register'
        self.user = create_user(
            username='test',
            email='test@djangotalents.com',
            password='test'
        )
        CaptchaStore(
            response='test-captcha-response',
            hashkey='test-captcha-hashkey',
        ).save()

    def test_correct_signup(self):
        data = {
            'username': 'kurtcobain',
            'email': 'kurt@nirvanatest.com',
            'password1': 'kurtNirvana2',
            'password2': 'kurtNirvana2',
            'country': 'MX',
            'captcha_0': 'test-captcha-hashkey',
            'captcha_1': 'test-captcha-response',
        }
        response = self.client.post(self.signup_url, follow=True, data=data)
        assert that(response.redirect_chain).equals([('http://testserver/accounts/register/complete/', 302)])
        assert that(response.content).contains('Your account has been successfully registered!')
        try:
            user = User.objects.get(username=data['username'], email=data['email'])
            profile = UserProfile.objects.get(user=user)
        except User.DoesNotExist:
            assert False, 'User with username "%s" was not created.' % data['username']
        except UserProfile.DoesNotExist:
            assert False, 'The profile for user <%s> could not be created.' % data['username']

    def test_empty_username(self):
        response = self.client.post(self.signup_url, follow=True, data={
            'username': '',
            'email': 'kurt@nirvanatest.com',
            'password1': 'kurtNirvana2',
            'password2': 'kurtNirvana2',
            'country': 'MX'
        })
        assert that(response.content).contains('You are a Django Talent?')
        assert that(response.content).contains('Username:')
        assert that(response.content).contains('This field is required.')

    def test_invalid_username(self):
        response = self.client.post(self.signup_url, follow=True, data={
            'username': 'kurt123$',
            'email': 'kurt@nirvanatest.com',
            'password1': 'kurtNirvana2',
            'password2': 'kurtNirvana2',
            'country': 'MX'
        })
        assert that(response.content).contains('You are a Django Talent?')
        assert that(response.content).contains('Username:')
        assert that(response.content).contains('This value may contain only letters, numbers and @/./+/-/_ characters.')

    def test_username_in_use(self):
        response = self.client.post(self.signup_url, follow=True, data={
            'username': 'test',
            'email': 'kurt@nirvanatest.com',
            'password1': 'kurtNirvana2',
            'password2': 'kurtNirvana2',
            'country': 'MX'
        })
        assert that(response.content).contains('You are a Django Talent?')
        assert that(response.content).contains('Username:')
        assert that(response.content).contains('A user with that username already exists.')

    def test_empty_email(self):
        response = self.client.post(self.signup_url, follow=True, data={
            'username': 'kurt',
            'email': '',
            'password1': 'kurtNirvana2',
            'password2': 'kurtNirvana2',
            'country': 'MX'
        })
        assert that(response.content).contains('You are a Django Talent?')
        assert that(response.content).contains('E-mail address:')
        assert that(response.content).contains('This field is required.')

    def test_invalid_email(self):
        response = self.client.post(self.signup_url, follow=True, data={
            'username': 'kurt',
            'email': 'kurt @ nirvanatest.com',
            'password1': 'kurtNirvana2',
            'password2': 'kurtNirvana2',
            'country': 'MX'
        })
        assert that(response.content).contains('You are a Django Talent?')
        assert that(response.content).contains('E-mail address:')
        assert that(response.content).contains('Enter a valid e-mail address.')

    def test_email_in_use(self):
        response = self.client.post(self.signup_url, follow=True, data={
            'username': 'kurt',
            'email': 'test@djangotalents.com',
            'password1': 'kurtNirvana2',
            'password2': 'kurtNirvana2',
            'country': 'MX'
        })
        assert that(response.content).contains('You are a Django Talent?')
        assert that(response.content).contains('E-mail address:')
        assert that(response.content).contains('User with this E-mail address already exists.')

    def test_passwords_dont_match(self):
        response = self.client.post(self.signup_url, follow=True, data={
            'username': 'kurtcobain',
            'email': 'kurt@nirvanatest.com',
            'password1': 'kurtNirvana2',
            'password2': 'kurt_nirvana3',
            'country': 'MX'
        })
        assert that(response.content).contains('You are a Django Talent?')
        assert that(response.content).contains('Password confirmation:')
        assert that(response.content).contains("The two password fields didn&#39;t match.")

    def test_empty_country(self):
        response = self.client.post(self.signup_url, follow=True, data={
            'username': 'kurtcobain',
            'email': 'kurt@nirvanatest.com',
            'password1': 'kurtNirvana2',
            'password2': 'kurtNirvana2',
            'country': ''
        })
        assert that(response.content).contains('You are a Django Talent?')
        assert that(response.content).contains('Country:')
        assert that(response.content).contains('This field is required.')

    def test_invalid_country(self):
        response = self.client.post(self.signup_url, follow=True, data={
            'username': 'kurtcobain',
            'email': 'kurt@nirvanatest.com',
            'password1': 'kurtNirvana2',
            'password2': 'kurtNirvana2',
            'country': 'XX'
        })
        assert that(response.content).contains('You are a Django Talent?')
        assert that(response.content).contains('Country:')
        assert that(response.content).contains('Select a valid choice. That choice is not one of the available choices.')
