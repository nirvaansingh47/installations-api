import json

from django.test import TestCase
from rest_framework.test import APIClient

from installations.api.models import Installation


class TestInstallationCreate(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_when_create_installation_should_set_default_status(self):
        installation = {
            'customer_name': 'John Smith',
            'appointment_date': '2021-02-21T09:00:00'
        }
        self.client.post('/create/installation/', installation)
        installation = Installation.objects.first()

        self.assertEqual(installation.statuses.get().status, 'installation_request')

    # pretty long name but it is mega descriptive.
    def test_when_updating_installation_status_should_create_new_record(self):
        installation = Installation.objects.create(customer_name='John Smith', appointment_date='2021-02-21T09:00:00')
        self.client.put('/create/installation/', {
            "installation": installation.pk,
            "status": "installation_complete",
            "notes": "Completed!",
            "date": "2020-01-30T10:00:00"
        })

        installation = Installation.objects.get(pk=installation.pk)
        self.assertEqual(installation.latest_status, 'installation_complete')
        self.assertEqual(installation.statuses.order_by('-date').first().status, 'installation_complete')


class TestInstallationHistory(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_when_retrieving_history_should_get_list(self):
        installation = {
            'customer_name': 'John Smith',
            'appointment_date': '2021-02-21T09:00:00'
        }
        self.client.post('/create/installation/', installation)
        installation = Installation.objects.get()
        self.client.put('/create/installation/', {
            "installation": installation.pk,
            "status": "installation_complete",
            "notes": "Completed!",
            "date": "2020-01-30T10:00:00"
        })

        response = self.client.get(f'/installations/{installation.pk}/history/')

        self.assertEqual(len(json.loads(response.content)), 2)