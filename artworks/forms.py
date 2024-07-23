from django import forms
from .models import Artwork, Category


class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = '__all__'
  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        category_choices = [(c.id, c.name) for c in categories]

        self.fields['category'].choices = category_choices
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
