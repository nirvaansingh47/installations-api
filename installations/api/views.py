from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from installations.api.models import Installation
from installations.api.serializers import InstallationSerializer, StatusSerializer


class CreateUpdateInstallationView(APIView):
    def post(self, request):
        serializer = InstallationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        installation = Installation.objects.create(**serializer.validated_data)

        return Response(data=InstallationSerializer(installation).data, status=status.HTTP_201_CREATED)

    def put(self, request):
        serializer = StatusSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            installation = Installation.objects.get(pk=serializer.validated_data.get('installation'))
            installation.statuses.create(
                status=serializer.validated_data.get('status'),
                notes=serializer.validated_data.get('notes'),
                date=serializer.validated_data.get('date'),
            )

            return Response(status=status.HTTP_200_OK)
        except Installation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
