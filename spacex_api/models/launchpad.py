from .base import Model, CharField


class Launchpad(Model):
    # Remove after switch to database data source
    _model_url_path = 'launchpads'

    id = CharField(max_length=255)
    full_name = CharField(max_length=255)
    status = CharField(max_length=255)
