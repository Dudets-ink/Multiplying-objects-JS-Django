from django import forms

class InputForm(forms.Form):
    """Text input form"""

    input_field = forms.CharField(max_length=200, label='Введите текст')
    widgets = {'input_field': forms.Textarea()}
