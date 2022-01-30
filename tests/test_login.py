from http import HTTPStatus

from django.contrib.auth import SESSION_KEY
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
        self.assertIn(SESSION_KEY, self.client.session)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'landing.html')

    def test_view_landing_with_logged_user(self):
        self.client.login(username='user', password='test')
        response = self.client.get('/', follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'landing.html')

    def test_view_services_with_logged_user(self):
        response = self.client.get('/services', follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'index.html')
