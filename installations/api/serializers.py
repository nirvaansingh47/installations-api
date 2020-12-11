from rest_framework import serializers

from installations.api.models import Installation


class InstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Installation
        fields = '__all__'

