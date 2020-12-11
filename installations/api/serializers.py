from rest_framework import serializers

from installations.api.models import Installation


class InstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Installation
        fields = '__all__'


class StatusSerializer(serializers.Serializer):
    installation = serializers.UUIDField()
    status = serializers.CharField()
    notes = serializers.CharField()
    date = serializers.DateTimeField()