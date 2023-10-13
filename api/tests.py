from django.contrib.auth.models import User
from django.test import TestCase
from api.views import login, logout, register_user
from rest_framework.test import APIRequestFactory
from rest_framework.authtoken.models import Token


class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test', password='test', email="test")

    def test_login(self):
        factory = APIRequestFactory()
        request = factory.post(
            '/auth/login/', {'email': 'test', 'password': 'test'})
        self.assertEqual(login(request).status_code, 200)

    def test_logout(self):
        factory = APIRequestFactory()
        request = factory.post('/auth/logout/')
        user = self.user
        token = Token.objects.create(user=user)
        request.META['HTTP_AUTHORIZATION'] = 'Token ' + token.key
        self.assertEqual(logout(request).status_code, 200)

    def test_register(self):
        factory = APIRequestFactory()
        request = factory.post(
            '/auth/register/', {'email': 'test2', 'password': 'test2', 'first_name': 'test2', 'last_name': 'test2'})
        self.assertEqual(register_user(request).status_code, 201)
