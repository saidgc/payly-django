from django.test import TestCase
from firebase_db.models.collections import Collections
import random

class TestCollections(TestCase):

    def setUp(self) -> None:
        self.collections = Collections()
        self.random_service = random.choice(
            list(
                self.collections.get_all_services().keys(),
            ),
        )

    def test_collections_instance(self):
        self.assertIsInstance(self.collections, Collections)

    def test_get_all_services(self):
        services = self.collections.get_all_services()
        self.assertIsInstance(services, dict)

    def test_get_service(self):
        service = self.collections.get_service(
            service_id=self.random_service,
        )
        self.assertIsInstance(service, dict)

    def test_get_service_with_none_service(self):
        service = self.collections.get_service(
            service_id='',
        )
        self.assertIsInstance(service, dict)

