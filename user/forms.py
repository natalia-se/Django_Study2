from django import forms
from .models import FormSubmission

class FormName(forms.ModelForm):
    class Meta:
        model = FormSubmission
        fields = ['name', 'email', 'text']