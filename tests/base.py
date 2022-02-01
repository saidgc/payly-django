from random import choice

from django.contrib.auth.models import User
from django.test import TestCase
from faker import Faker

from firebase_db.models.collections import Collections

fake = Faker()


class PrepareTestUser(TestCase):
    password = None
    user_name = None
    firestore_fake_id = fake.uuid4()

    @classmethod
    def setUpTestData(cls):
        cls.user_name = fake.user_name()
        cls.password = 'password'
        cls.user = User.objects.create_user(
            username=cls.user_name,
            password=cls.password,
        )


class PrepareTestFirestore(TestCase):
    collections = Collections()

    @classmethod
    def setUpTestData(cls):
        cls.service_id = choice(
            list(
                cls.collections.get_all_services().keys(),
            ),
        )
