from django import forms
from .models import Targets

class IndexForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the star name.")

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Targets
        fields = "__all__"


