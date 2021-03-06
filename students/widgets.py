from django import forms

class InputMaskWidget(forms.TextInput):
    def get_context(self, name, value, attrs):
        attrs['data-custom-widget'] = self.__class__.__name__
        return super().get_context(name, value, attrs)

    class Media:
        js = ('AdminLTE-3.0.5/plugins/inputmask/inputmask.min.js',
              'AdminLTE-3.0.5/plugins/inputmask/bindings/inputmask.binding.js')

class DatePickerWidget(forms.DateInput):
    def get_context(self, name, value, attrs):
        attrs['data-custom-widget'] = self.__class__.__name__
        attrs['data-inputmask'] = "'alias': 'datetime', 'inputFormat': 'isoDate'"
        context = super().get_context(name, value, attrs)
        return context

    class Media:
        js = ('AdminLTE-3.0.5/plugins/jquery/jquery.min.js', 'AdminLTE-3.0.5/plugins/moment/moment.min.js',
              'AdminLTE-3.0.5/plugins/daterangepicker/daterangepicker.js',
              'AdminLTE-3.0.5/plugins/inputmask/inputmask.min.js', 'js/widgets/datepickerwidget.js')