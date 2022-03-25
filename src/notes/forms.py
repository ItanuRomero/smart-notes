from django import forms
from django.core.exceptions import ValidationError

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={'class': 'form-control my-5'})
        }
        labels = {
            'text': 'What are you thinking?'
        }
        
    def clean_title(self):
        title =self.cleaned_data['title']
        if 'django' not in title.lower():
            raise ValidationError('We only accept notes about Django!')
        return title
        