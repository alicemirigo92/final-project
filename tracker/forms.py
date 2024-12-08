from django import forms
from .models import Activity, Badge

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['activity_type', 'value', 'unit']

class BadgeForm(forms.ModelForm):
    class Meta:
        model = Badge
        fields = ['name', 'description']
