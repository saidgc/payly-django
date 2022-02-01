import random

from django.test import TestCase

from firebase_db.models.collections import Collections
from tests.base import PrepareTestFirestore


class TestCollections(PrepareTestFirestore):

    def test_collections_instance(self):
        self.assertIsInstance(self.collections, Collections)

    def test_get_all_services(self):
        services = self.collections.get_all_services()
        self.assertIsInstance(services, dict)

    def test_get_service(self):
        service = self.collections.get_service(
            service_id=self.service_id,
        )
        self.assertIsInstance(service, dict)

    def test_get_service_with_none_service(self):
        service = self.collections.get_service(
            service_id='',
        )
        self.assertIsInstance(service, dict)
