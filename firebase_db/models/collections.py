from google.cloud import firestore


class Collections:
    def __init__(self):
        self.client = firestore.Client()

    def get_all_services(self):
        services_ref = self.client.collection(u'services')
        services = services_ref.where(u'active', u'==', True).stream()
        return [service.to_dict() for service in services]
