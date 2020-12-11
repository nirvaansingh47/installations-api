from datetime import datetime

from rest_framework import status, viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from installations.api.models import Installation
from installations.api.serializers import InstallationSerializer, StatusSerializer, InstallationReadSerializer, \
    StatusListSerializer


class CreateUpdateInstallationView(APIView):
    def post(self, request):
        serializer = InstallationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        installation = Installation.objects.create(**serializer.validated_data)

        installation.statuses.create(
            status='installation_request',
            notes='Installation created.',
        )

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
            installation.date_modified = datetime.now()
            installation.save()

            return Response(status=status.HTTP_200_OK)
        except Installation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ListRetrieveInstallationView(viewsets.ReadOnlyModelViewSet):
    queryset = Installation.objects.order_by('-date_modified')
    serializer_class = InstallationReadSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['appointment_date', 'date_modified']

    @action(detail=True, methods=['GET'])
    def history(self, request, pk):
        obj = self.get_object()
        history = StatusListSerializer(obj.get_history(), many=True)

        return Response(data=history.data, status=status.HTTP_200_OK)
