from unittest.mock import Mock

from django.test import TestCase

from firebase_db.models.authentication import FirebaseAuthentication


class TestAuthentication(TestCase):
    def setUp(self) -> None:
        self.mock = FirebaseAuthentication()

    def test_login_function_fails(self):
        resp = self.mock.login(
            request=Mock(),
            user='fake@mail.com',
            email='fake@mail.com',
            password='123asdbASDB',
        )
        self.assertFalse(resp)



