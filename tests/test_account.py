from http import HTTPStatus

from django.contrib.auth import SESSION_KEY
from django.test import TestCase
from faker import Faker

from firebase_db.models.authentication import FIREBASE_KEY
from .base import PrepareTestUser

fake = Faker()


class TestAccount(TestCase):

    def test_view_account_without_login(self):
        response = self.client.get('/account', follow=True)
        self.assertRedirects(response, '/login/', HTTPStatus.MOVED_PERMANENTLY)


class TestAccountLoggedUser(PrepareTestUser):

    def setUp(self) -> None:
        self.client.login(
            username=self.user_name,
            password=self.password,
        )
        session = self.client.session
        session[FIREBASE_KEY] = self.firestore_fake_id
        session.save()

    def test_view_account_with_login(self):
        response = self.client.get('/account', follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'account.html')
        self.assertIn(SESSION_KEY, self.client.session)
