from http import HTTPStatus

from django.test import TestCase


class TestServices(TestCase):

    def test_view_service(self):
        response = self.client.get('/services', follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'index.html')

