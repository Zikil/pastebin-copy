from django import forms
from .models import Paste

class PasteForm(forms.ModelForm):

    class Meta:
        model = Paste
        fields = ['body', 'title', 'life_time', 'access']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            # 'author': forms.TextInput(attrs={'class': 'form-control'}),
            'life_time': forms.Select(attrs={'class': 'form-control'}),
            'access': forms.Select(attrs={'class': 'form-control'}),
        }
