from http import HTTPStatus

from django.test import TestCase


class TestLanding(TestCase):

    def test_view_landing(self):
        response = self.client.get('/', follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'landing/landing.html')
