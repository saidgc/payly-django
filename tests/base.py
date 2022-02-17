from random import choice

from django.test import TestCase
from faker import Faker

from apps.account.models import PaylyUser as User
from apps.firebase_db.models.collections import Payment, Service

fake = Faker()


class PrepareTestUser(TestCase):
    password = None
    user_name = None

    @classmethod
    def setUpTestData(cls):
        cls.user_name = fake.user_name()
        cls.password = 'password'
        cls.user = User.objects.create_user(
            username=cls.user_name,
            password=cls.password,
            firebase_user_id=fake.uuid4(),
        )


class PrepareTestFirestore(TestCase):
    services = Service()
    payments = Payment()
    customer_id = 'nPzc4Bq38VNSLuKSJ7GXZhss1vg2'

    @classmethod
    def setUpTestData(cls):
        cls.service_id = choice(
            list(
                cls.services.get_all_services().keys(),
            ),
        )
