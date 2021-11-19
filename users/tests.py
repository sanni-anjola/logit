from django.test import TestCase

# Create your tests here.
from django.urls import reverse

from users.models import Account


class AccountTestCase(TestCase):
    def setUp(self) -> None:
        user1 = Account.objects.create(email="john_doe@email.com", password="123Pass321")
        user2 = Account.objects.create(email="james@email.com", password="123Pass321")
        user3 = Account.objects.create(email="peter@email.com", password="123Pass321")

    def test_create_account(self):
        data = {
            "email": "janet@gmail.com",
            "password": "ghgshshsye__teyey",
        }

        response = self.client.post(reverse('create_account'), data=data)
        print(response.status_code)
        print((reverse('create_account')))
