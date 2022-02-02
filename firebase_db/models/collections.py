from google.cloud import firestore


class FirestoreCollection:
    def __init__(self, collection: str) -> None:
        self.collection = firestore.Client().collection(collection)


class Service(FirestoreCollection):

    def __init__(self):
        super().__init__(u'services')

    def get_all_services(self) -> dict:
        all_services = {}
        services = self.collection.\
            where(u'active', u'==', True).\
            stream()
        for service in services:
            all_services[service.id] = service.to_dict()
        return all_services

    def get_service(self, service_id: str) -> dict:
        if not service_id:
            return {}
        service = self.collection.document(
            document_id=service_id,
        ).get().to_dict()
        return service


class Payment(FirestoreCollection):

    def __init__(self):
        super().__init__(u'payments')

    def get_all_payments(self) -> dict:
        all_payments = {}
        payments = self.collection.stream()
        for payment in payments:
            all_payments[payment.id] = payment.to_dict()
        return all_payments

    def get_payments_by_customer(self, customer_id: str) -> dict:
        all_payments = {}
        payments = self.collection.\
            where(u'user', u'==', customer_id).\
            order_by('payment_date').\
            stream()
        for payment in payments:
            all_payments[payment.id] = payment.to_dict()
        return all_payments
