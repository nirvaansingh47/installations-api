import uuid

from django.db import models


class Installation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer_name = models.CharField(max_length=64)
    appointment_date = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    latest_status = models.CharField(max_length=32, default='installation_request')

    def get_history(self):
        return self.statuses.order_by('-date')


class InstallationStatus(models.Model):
    INSTALLATION_STATUS_CHOICES = (
        ('installation_request', 'Installation requested'),
        ('installation_in_progress', 'Installation in progress'),
        ('installation_complete', 'Installation Complete'),
        ('installation_rejected', 'Installation Rejected'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=32, choices=INSTALLATION_STATUS_CHOICES)
    notes = models.TextField()
    date = models.DateTimeField(auto_now=True)
    installation = models.ForeignKey(Installation, related_name='statuses', on_delete=models.CASCADE)
