import logging

from django.conf import settings
import requests

from utils.rest_api_db.models import RestApiCharField, RestApiManager, RestApiModel


log = logging.getLogger(__name__)


# Change base class to django.db.models.Manager for database data source.
class Manager(RestApiManager):
    """
    Base class for all custom managers.
    """


# Change base class to django.db.models.Model for database data source.
class Model(RestApiModel):
    """
    Base class for all data access models.
    """
    #
    # This is all SpaceX API specific code for the RestApiDb layer.
    #
    # Remove after switch to database data store.
    #
    _url_prefix = settings.SPACEX_API_URL_PREFIX
    _model_url_path = ''

    @classmethod
    def fetch_api_results(cls, **conditions):
        url = f'{cls._url_prefix}/{cls._model_url_path}/query'

        params = {'query': conditions, 'options': {'pagination': False}}

        log.info(f"Fetching data from {url} with parameters: {repr(params)}")
        return requests.post(url, json=params).json()['docs']

    @staticmethod
    def translate_query_params_to_conditions(params):
        return {field_name: {'$in': values} if len(values) > 1 else values[0]
                for field_name, values in params.lists()}


# Change base class to django.db.models.CharField for database source.
class CharField(RestApiCharField):
    """
    Base class for all model character fields.
    """
