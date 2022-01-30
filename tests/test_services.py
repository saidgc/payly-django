from http import HTTPStatus
from random import choice

from django.test import TestCase

from firebase_db.models.collections import Collections


class TestServices(TestCase):

    def setUp(self) -> None:
        self.service_id = choice(
            list(
                Collections().get_all_services().keys(),
            ),
        )

    def test_view_service(self):
        response = self.client.get('/services', follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'index.html')

    def test_view_pay_service(self):
        payload = {
            'id': self.service_id
        }
        response = self.client.post('/pay', payload, follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'pay_service.html')

    def test_view_pay_service_without_service_id(self):
        payload = {
            'id': ''
        }
        response = self.client.post('/pay', payload, follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'index.html')
