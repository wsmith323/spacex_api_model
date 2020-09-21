from ..models import Launchpad
from ..serializers import LaunchpadSerializer

from .base import ModelViewSet


class LaunchpadViewSet(ModelViewSet):
    queryset = Launchpad.objects.all()
    serializer_class = LaunchpadSerializer
