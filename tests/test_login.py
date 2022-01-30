from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import TestCase


class TestLogin(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='user',
            password='test',
        )

    def test_view_login(self):
        response = self.client.get('/login', follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'login.html')

    def test_view_login_with_logged_user(self):
        self.client.login(username='user', password='test')
        response = self.client.get('/login', follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'landing.html')


