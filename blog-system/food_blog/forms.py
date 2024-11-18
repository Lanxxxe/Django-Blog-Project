from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'content']  # Updated field names
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Comment', 'rows': 1, 'style' : 'resize: none;'}),
        }