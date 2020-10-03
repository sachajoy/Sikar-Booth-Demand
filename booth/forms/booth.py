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
            'route_no': forms.TextInput(),
            'uid': forms.TextInput(attrs={'disabled': 'disabled'}),
            'upwd': forms.PasswordInput(attrs={'disabled': 'disabled'}),
            'active': forms.CheckboxInput(attrs={'disabled': 'disabled'})
        }
        labels = {
            'route_no': 'Route No.',
            'booth_no': 'Booth No',
            'xname': 'Name',
            'add1': 'Add 1',
            'add2': 'Add 2',
            'add3': 'Add 3',
            'add4': 'Add 4',
            'mobile': 'Mobile',
            'uid': 'Login',
            'upwd': 'Password',
            'active': 'Active',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'form-control form-control-user'}
            )
