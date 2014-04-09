# -*- coding: utf-8 -*-
from django.core import exceptions
from django.db import models
from django.utils.translation import gettext as _
from .version import Version


class VersionField(models.CharField):
    __metaclass__ = models.SubfieldBase
    default_error_messages = {
        'invalid': _("Enter a valid version number in X.Y.Z format."),
    }
    description = _("Version")

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 50)
        super(VersionField, self).__init__(*args, **kwargs)

    def get_prep_value(self, obj):
        return str(obj)

    def to_python(self, value):
        if value is None or value == '':
            return None
        if isinstance(value, Version):
            return value
        return Version(value)

    def get_db_prep_value(self, value, connection, prepared=False):
        if not prepared:
            value = self.get_prep_value(value)
        return value

    def value_to_string(self, obj):
        value = self.to_python(self._get_val_from_obj(obj))
        return str(value)

    def run_validators(self, value):
        return super(VersionField, self).run_validators(str(value))

    def validate(self, value, model_instance):
        if not self.editable:
            return
        if value is None and not self.null:
            raise exceptions.ValidationError(self.error_messages['null'], code='null')

        if not self.blank and str(value) in self.empty_values:
            raise exceptions.ValidationError(self.error_messages['blank'], code='blank')

        if not (value.major or value.minor or value.release):
            raise exceptions.ValidationError(self.error_messages['invalid'], code='invalid')


def add_south_rules():
    from south.modelsinspector import add_introspection_rules

    add_introspection_rules([((VersionField,),
                              [],
                              {},), ], ["whatsnew\.fields"])


try:  # pragma: no cover
    import south
except ImportError:  # pragma: no cover
    south = None

if south:  # pragma: no cover
    add_south_rules()
