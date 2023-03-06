from django.forms import ModelForm

from .models import VisitorUrl


class VisitorUrlForm(ModelForm):
    class Meta:
        model = VisitorUrl
        fields = ['origin_url', 'name']
