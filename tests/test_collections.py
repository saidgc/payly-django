from django.test import TestCase
from firebase_db.models.collections import Collections


class TestCollections(TestCase):

    def setUp(self) -> None:
        self.collections = Collections()

    def test_collections_instance(self):
        self.assertIsInstance(self.collections, Collections)

    def test_get_all_services(self):
        services = self.collections.get_all_services()
        self.assertIsInstance(services, list)

