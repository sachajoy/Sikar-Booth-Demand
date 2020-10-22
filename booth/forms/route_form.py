from django import forms
from django.forms.models import ModelForm

from booth import models

class RouteCreateForm(ModelForm):
    class Meta:
        model = models.Route
        fields = [
            'xname', 'route_no',
            'contractor_id', 'active'
        ]
        labels = {
            'xname': 'Route Name',
            'route_no': 'Route Name',
            'contractor_id': 'Contractor',
            'active': 'Active'
        }
        widgets = {
            'active': forms.CheckboxInput(attrs={'disabled': 'disabled'})
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for name, field in self.fields.items():
                field.widget.attrs.update(
                    {'class': 'form-control form-control-user'}
                )