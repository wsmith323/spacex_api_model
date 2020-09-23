from django.http import QueryDict
from django.test import TestCase

from ..models.base import Model


class BaseModelTestCase(TestCase):
    def setUp(self):
        self.test_params = QueryDict('test1=value1&test2=value1&test2=value2')
        self.expected_conditions = {'test1': 'value1', 'test2': {'$in': ['value1', 'value2']}}

    def test_params_to_conditions(self):
        conditions = Model.translate_query_params_to_conditions(self.test_params)
        self.assertDictEqual(conditions, self.expected_conditions)
