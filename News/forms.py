from .models import Articles
from django.forms import ModelForm,TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title','anons','full_text','date']

        widgets={
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Name',
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter anons of news',
            }),
            "date": DateTimeInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'datetime-local'  
            }),
            
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "text of the news",
            }),

    }