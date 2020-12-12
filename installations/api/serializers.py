from rest_framework import serializers

from installations.api.models import Installation


class InstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Installation
        fields = '__all__'


class InstallationReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Installation
        fields = (
            'id',
            'customer_name',
            'appointment_date',
            'date_created',
            'date_modified',
            'latest_status'
        )


class StatusSerializer(serializers.Serializer):
    installation = serializers.UUIDField()
    status = serializers.CharField()
    notes = serializers.CharField()


class StatusListSerializer(serializers.Serializer):
    status = serializers.CharField()
    notes = serializers.CharField()
    date = serializers.DateTimeField()
