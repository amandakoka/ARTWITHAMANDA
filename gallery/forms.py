# gallery/forms.py

from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['artwork', 'text']
        widgets = {
            'artwork': forms.Select(),
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Leave your review here...'}),
        }
