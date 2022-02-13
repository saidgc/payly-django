from http import HTTPStatus

from django.contrib.auth import SESSION_KEY
from django.test import TestCase
from django.urls import reverse
from faker import Faker

from tests.base import PrepareTestUser

fake = Faker()


class TestPayTelmexWithoutLogin(TestCase):

    def test_view_without_login(self):
        response = self.client.get(reverse('collaborator_pay_service', args=['6IpK0smbJQ00mAeDa81g']), follow=True)
        self.assertRedirects(response, '/login/')

    def test_view_without_login_args(self):
        response = self.client.get(reverse('collaborator_pay_service'), follow=True)
        self.assertRedirects(response, '/login/')


class TestPayTelmex(PrepareTestUser):

    def setUp(self) -> None:
        self.client.login(
            username=self.user_name,
            password=self.password,
        )
        session = self.client.session
        session.save()

    def test_view(self):
        response = self.client.get(reverse('collaborator_pay_service', args=['6IpK0smbJQ00mAeDa81g']), follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'collaborator/services/telmex.html')
        self.assertIn(SESSION_KEY, self.client.session)
