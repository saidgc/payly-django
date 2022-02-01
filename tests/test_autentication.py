from unittest.mock import Mock

from django.test import TestCase
from faker import Faker

from firebase_db.models.authentication import FirebaseAuthentication

fake = Faker()


class TestAuthentication(TestCase):
    def setUp(self) -> None:
        self.mock = FirebaseAuthentication()
        self.user_name = fake.user_name()
        self.email = fake.email()
        self.password = 'password'

    def test_login_function_fails(self):
        resp = self.mock.login(
            request=Mock(),
            user=self.user_name,
            email=self.email,
            password=self.password,
        )
        self.assertFalse(resp)



