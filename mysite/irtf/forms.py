from django import forms
from .models import Targets

class IndexForm(forms.ModelForm):
    #name = forms.CharField(max_length=128, help_text="Please enter the star name.")
    teff_min = forms.CharField()
    teff_max = forms.CharField()

    logg_min = forms.CharField()
    logg_max = forms.CharField()

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Targets
        fields = "__all__"

class DownloadForm(forms.Form):
    #name = forms.CharField(max_length=128, help_text="Please enter the star name.")
    teff_min = forms.CharField(widget=forms.HiddenInput)
    teff_max = forms.CharField(widget=forms.HiddenInput)

    logg_min = forms.CharField(widget=forms.HiddenInput)
    logg_max = forms.CharField(widget=forms.HiddenInput)


