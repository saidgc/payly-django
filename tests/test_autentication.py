from unittest.mock import Mock

from django.test import TestCase

from firebase_db.models.authentication import login


class TestAuthentication(TestCase):

    def test_login_function_fails(self):
        resp = login(
            request=Mock(),
            user='fake@mail.com',
            email='fake@mail.com',
            password='123asdbASDB',
        )
        self.assertFalse(resp)



