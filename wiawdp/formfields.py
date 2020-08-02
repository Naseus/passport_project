from django.forms.fields import CharField
import django.forms.fields

from wiawdp import widgets
from wiawdp.validators import ZIPCodeValidator, SSNValidator


class EmailField(django.forms.fields.EmailField):
    widget = widgets.InputMaskWidget(
        attrs={'autocomplete': 'off', 'data-inputmask-alias': 'email',
               'pattern': r'.+@.+\.[A-Za-z]([A-Za-z0-9\-]*[A-Za-z0-9])?'})

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class SSNField(CharField):
    widget = widgets.InputMaskWidget(attrs={'autocomplete': 'off', 'data-inputmask-alias': 'ssn',
                                            'pattern': SSNValidator.regex})

    def __init__(self, min_length=9, max_length=11, **kwargs):
        super().__init__(min_length=min_length, max_length=max_length, **kwargs)

    def clean(self, value):
        value = super(SSNField, self).clean(value)
        return value.replace('-', '')


class ZIPCodeField(CharField):
    widget = widgets.InputMaskWidget(
        attrs={'autocomplete': 'off', 'data-inputmask-mask': '99999',
               'pattern': ZIPCodeValidator.regex})

    def __init__(self, min_length=5, max_length=5, **kwargs):
        super().__init__(min_length=min_length, max_length=max_length, **kwargs)
