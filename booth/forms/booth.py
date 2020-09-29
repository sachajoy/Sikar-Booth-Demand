from django.forms.models import ModelForm
from django import forms
from booth import models


class BoothForm(ModelForm):
    class Meta:
        fields = [
            'route_no', 'booth_no',
            'xname', 'add1', 'add2',
            'add3', 'add4', 'mobile',
            'uid', 'upwd', 'active',
        ]
        models = models.Booth
        widgets = {
            'uid': forms.CharField(attrs={'disabled':'disabled'}),
            'upwd': forms.PasswordInput(attrs={'disabled':'disabled'}),
            'active': forms.CheckboxInput(attrs={'disabled':'disabled'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.item():
            field.widget.attrs.update(
                {'class': 'form-control form-control-user'}
            )