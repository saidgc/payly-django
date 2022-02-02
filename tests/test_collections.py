from firebase_db.models.collections import FirestoreCollection
from tests.base import PrepareTestFirestore


class TestCollections(PrepareTestFirestore):

    def test_collections_instance(self):
        self.assertIsInstance(self.payments, FirestoreCollection)
        self.assertIsInstance(self.services, FirestoreCollection)

    def test_get_all_services(self):
        services = self.services.get_all_services()
        self.assertIsInstance(services, dict)

    def test_get_service(self):
        service = self.services.get_service(
            service_id=self.service_id,
        )
        self.assertIsInstance(service, dict)

    def test_get_service_with_none_service(self):
        service = self.services.get_service(
            service_id='',
        )
        self.assertIsInstance(service, dict)

    def test_get_all_payments(self):
        payments = self.payments.get_all_payments()
        self.assertIsInstance(payments, dict)

    def test_get_payments_by_customer(self):
        payments = self.payments.get_payments_by_customer(self.customer_id)
        self.assertIsInstance(payments, dict)
