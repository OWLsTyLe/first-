from .models import Category
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name_you', 'pud_text', 'pub_date']

        widgets = {
            'name_you': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Імʼя'
            }),
            'pud_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Повідомлення'
            }),
            'pub_date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата відправки'
            })
        }

