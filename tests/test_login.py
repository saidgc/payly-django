from http import HTTPStatus

from django.contrib.auth import SESSION_KEY
from django.test import TestCase
from faker import Faker

from firebase_db.models.authentication import FIREBASE_KEY
from tests.base import PrepareTestUser

fake = Faker()


class TestLoginView(TestCase):

    def test_view_login(self):
        response = self.client.get('/login', follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'login.html')


class TestLogin(PrepareTestUser):

    def setUp(self):
        self.client.login(
            username=self.user_name,
            password=self.password,
        )
        session = self.client.session
        session[FIREBASE_KEY] = self.firestore_fake_id
        session.save()

    def test_view_login_with_logged_user(self):
        response = self.client.get('/login', follow=True)
        self.assertRedirects(response, '/services/', HTTPStatus.MOVED_PERMANENTLY)
        self.assertIn(SESSION_KEY, self.client.session)
        self.assertIn(FIREBASE_KEY, self.client.session)

    def test_view_landing_with_logged_user(self):
        response = self.client.get('/', follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'landing.html')
        self.assertIn(SESSION_KEY, self.client.session)
        self.assertIn(FIREBASE_KEY, self.client.session)

    def test_view_services_with_logged_user(self):
        response = self.client.get('/services', follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIn(SESSION_KEY, self.client.session)
        self.assertIn(FIREBASE_KEY, self.client.session)

