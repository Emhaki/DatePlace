from django import forms
from .models import DatePlace

class DatePlaceForm(forms.ModelForm):
    class Meta:
        model = DatePlace
        fields = ['name', 'category', 'address', 'description', 'rating', 'latitude', 'longitude', 'region']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

