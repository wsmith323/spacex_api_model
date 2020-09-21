from utils.rest_api_db.views import RestApiModelViewSet


# Change base class to rest_framework.viewsets.ModelViewSet for database data source.
class ModelViewSet(RestApiModelViewSet):
    """
    Base class for all model viewsets
    """
