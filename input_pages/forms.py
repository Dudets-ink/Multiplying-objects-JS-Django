from django import forms

class InputForm(forms.Form):
    """Text input form, contain a charField."""

    input_field = forms.CharField(max_length=150, label='Input text:')
    input_field.widget.attrs['required'] = 'required'


InputFormset = forms.formset_factory(InputForm)