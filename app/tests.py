from datetime import date

from django.test import TestCase

from app.models import Client


class ClientTestCase(TestCase):
    def setUp(self):
        Client.objects.create(
            first_name='first_name1',
            last_name='last_name1',
            address='address1',
            date_of_birth=date(2000, 12, 12)
        )

    def test_client_zodiac(self):
        client1 = Client.objects.get(address='address1')
        self.assertEqual(client1.zodiac, 'Sagittarius, \u2650')
