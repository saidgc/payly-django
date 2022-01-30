from http import HTTPStatus

from django.contrib.auth import SESSION_KEY
from django.contrib.auth.models import User
from django.test import TestCase


class TestLogout(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='user',
            password='test',
        )

    def test_view_logout(self):
        response = self.client.get('/logout', follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'index.html')

    def test_view_logout_with_logged_user(self):
        self.client.login(username='user', password='test')
        response = self.client.get('/logout', follow=True)
        self.assertNotIn(SESSION_KEY, self.client.session)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'index.html')






