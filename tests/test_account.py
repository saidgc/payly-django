from http import HTTPStatus

from django.test import TestCase
from django.contrib.auth.models import User
from firebase_db.models.authentication import FIREBASE_KEY


class TestAccount(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='user',
            password='test',
        )

    def test_view_account_without_login(self):
        response = self.client.get('/account', follow=True)
        self.assertRedirects(response, '/login/', HTTPStatus.MOVED_PERMANENTLY)

    def test_view_account_with_login(self):
        self.client.login(username='user', password='test')
        session = self.client.session
        session[FIREBASE_KEY] = '123abcd'
        session.save()
        response = self.client.get('/account', follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'account.html')
