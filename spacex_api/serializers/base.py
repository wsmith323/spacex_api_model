from utils.rest_api_db.serializers import RestApiModelSerializer


# Change base class to rest_framework.serializers.ModelSerializer for database data source.
class ModelSerializer(RestApiModelSerializer):
    """
    Base class for all model serializers
    """
