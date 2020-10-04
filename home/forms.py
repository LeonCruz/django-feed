from django import forms

from home.models import Site


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ('name', 'rss_site')
