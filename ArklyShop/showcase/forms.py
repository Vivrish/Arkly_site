from django import forms
from . import models


class DDMenuForm(forms.ModelForm):
    class Meta:
        model = models.Stock
        fields = ['sort']
