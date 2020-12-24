from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Purchase
from django.test import TestCase
from django.urls import reverse


class IndexViewTests(TestCase):
    def test_no_products(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['products'], [])

class PurchaseTest(TestCase):
    def test_no_purchase(self):
        response = self.client.get(reverse('mypurchase'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['purchase'], [])

class BuyTest(TestCase):
    def test_no_buy(self):
        response = self.client.get(reverse('buy', kwargs={'product_id': 0}))
        self.assertEqual(response.status_code, 200)

class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'
        }
        User.objects.create_user(**self.credentials)
    def test_login(self):
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)

class RegisterTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'email':'testuser@mail.ru',
            'password1': '400120Pav98',
            'password2': '400120Pav98'
        }
    def test_registration(self):
        response = self.client.post(reverse('register'), self.credentials)
        self.assertEqual(response.status_code, 302)
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)

