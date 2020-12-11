from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from installations.api.models import Installation
from installations.api.serializers import InstallationSerializer


class CreateUpdateInstallationView(mixins.CreateModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = Installation.objects.all()
    serializer_class = InstallationSerializer
