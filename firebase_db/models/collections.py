from google.cloud import firestore


class Collections:
    def __init__(self):
        self.client = firestore.Client()

    def get_all_services(self) -> dict:
        all_services = {}
        services_ref = self.client.collection(u'services')
        services = services_ref.where(u'active', u'==', True).stream()
        for service in services:
            all_services[service.id] = service.to_dict()
        return all_services

    def get_service(self, service_id: str) -> dict:
        if not service_id:
            return {}
        service = self.client.collection(
            u'services'
        ).document(
            service_id
        ).get().to_dict()
        return service
