from http import HTTPStatus

from django.contrib.auth import SESSION_KEY
from django.test import TestCase
from faker import Faker

from tests.base import PrepareTestUser

fake = Faker()


class TestLogoutView(TestCase):

    def test_view_logout(self):
        response = self.client.get('/logout', follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'index.html')


class TestLogout(PrepareTestUser):

    def setUp(self):
        self.client.login(
            username=self.user_name,
            password=self.password,
        )
        session = self.client.session
        session.save()

    def test_view_logout_with_logged_user(self):
        response = self.client.get('/logout', follow=True)
        self.assertNotIn(SESSION_KEY, self.client.session)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'index.html')
