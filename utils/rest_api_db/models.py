"""
Minimal Django-ORM-style api wrapper around restful web service.
"""


class RestApiQuery:
    def __init__(self, manager, results=None):
        self.manager = manager
        self._results = results

    def __iter__(self):
        if self._results is None:
            raise Exception('Query is not iterable.')
        return iter(self._results)

    def filter(self, **conditions):
        if self._results is None:
            results = [self.manager.model(result)
                       for result in self.manager.model.fetch_api_results(**conditions)]
            return type(self)(self.manager, results)
        else:
            return self

    def all(self):
        return self.filter()


class RestApiManager:
    def __init__(self, model):
        self.model = model

    def filter(self, **kwargs):
        return RestApiQuery(self).filter(**kwargs)

    def all(self):
        return RestApiQuery(self)


class RestApiField:
    field_name = None

    def __init__(self, *args, **kwargs):
        # Make constructor signature compatible with any arguments.
        pass

    def get_value(self, model, data):
        try:
            return data[self.field_name]
        except KeyError:
            raise AttributeError(f"{repr(model)} does not have attribute '{self.field_name}'")


class RestApiModelMeta(type):
    def __new__(mcs, name, bases, attrs, **kwargs):
        fields = {}
        for attr_name, attr_value in list(attrs.items()):
            if isinstance(attr_value, RestApiField):
                attr_value.field_name = attr_name
                fields[attr_name] = attr_value
                del attrs[attr_name]
        if fields:
            attrs['_fields'] = fields

        return super().__new__(mcs, name, bases, attrs)

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls.objects = RestApiManager(cls)


class RestApiModel(metaclass=RestApiModelMeta):
    _fields = {}
    _url_prefix = ''

    def __init__(self, data):
        self._data = data

    def __getattr__(self, item):
        field = self._fields.get(item, None)
        if field:
            return field.get_value(self, self._data)
        else:
            raise AttributeError(f"{repr(self)} does not have attribute '{item}'")

    @staticmethod
    def translate_query_params_to_conditions(params):
        return params


class RestApiCharField(RestApiField):
    def get_value(self, model, data):
        return str(super().get_value(model, data))


# Additional field classes for other data types,
# like booleans, integers, floats, dates, and times.
# ...

