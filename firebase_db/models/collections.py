from google.cloud import firestore


class Collections:
    def __init__(self):
        self.services_collection = firestore.Client().collection(u'services')

    def get_all_services(self) -> dict:
        all_services = {}
        services = self.services_collection.where(u'active', u'==', True).stream()
        for service in services:
            all_services[service.id] = service.to_dict()
        return all_services

    def get_service(self, service_id: str) -> dict:
        if not service_id:
            return {}
        service = self.services_collection.document(
            document_id=service_id
        ).get().to_dict()
        return service
