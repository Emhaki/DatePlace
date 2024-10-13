from django import forms
from .models import DatePlace

class DatePlaceForm(forms.ModelForm):
    class Meta:
        model = DatePlace
        fields = ['name', 'category', 'address', 'description', 'rating', 'latitude', 'longitude', 'region']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '장소 이름을 입력하세요'}),
            'address': forms.TextInput(attrs={'placeholder': '주소를 입력하세요'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': '장소에 대한 설명을 입력하세요'}),
            'rating': forms.NumberInput(attrs={'min': 0, 'max': 5, 'step': 0.1}),
            'latitude': forms.NumberInput(attrs={'readonly': 'readonly'}),
            'longitude': forms.NumberInput(attrs={'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['region'].widget.attrs.update({'class': 'form-select'})
        self.fields['category'].widget.attrs.update({'class': 'form-select'})
