from rest_framework.serializers import CharField

from ..models import Launchpad

from .base import ModelSerializer


class LaunchpadSerializer(ModelSerializer):
    id = CharField()
    name = CharField(source='full_name')
    status = CharField()

    class Meta:
        model = Launchpad
        fields = ['id', 'name', 'status']
