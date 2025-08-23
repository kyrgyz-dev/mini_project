from django import forms
from post.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', "category"]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'id': 'title'}),
            'content': forms.Textarea(attrs={'class': 'form-input', 'id': 'content'}),
            'category': forms.Select(attrs={'class': 'form-input', 'id': 'category'}),
        }
        labels = {
            'title': "Заголовок",
            'content': "Содержание",
            'category': "Категория",
        }

