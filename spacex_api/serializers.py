from rest_framework.serializers import CharField, Serializer


class LaunchpadSerializer(Serializer):
    id = CharField()
    name = CharField(source='full_name')
    status = CharField()
