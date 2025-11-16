from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

    # Example of basic input validation
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if "<" in title or ">" in title:
            raise forms.ValidationError("Invalid characters in title.")
        return title
