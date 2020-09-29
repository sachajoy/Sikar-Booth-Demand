from django import forms
from django.forms.models import ModelForm

from booth import models


class BoothForm(ModelForm):
    class Meta:
        fields = [
            'route_no', 'booth_no',
            'xname', 'add1', 'add2',
            'add3', 'add4', 'mobile',
            'uid', 'upwd', 'active',
        ]
        model = models.Booth
        widgets = {
            'uid': forms.TextInput(),
            'upwd': forms.PasswordInput(),
            'active': forms.CheckboxInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'form-control form-control-user'}
            )
