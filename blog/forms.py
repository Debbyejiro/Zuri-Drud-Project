from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class CommentForm(forms.ModelForm):
        content = forms.CharField(widget=forms.Textarea(attrs={
            'class': 'md-textarea form-control',
            'placeholder': 'comment here ...',
            'rows': '4',
        }))

    class Meta:
        model = Comment
        fields = ['author', 'post', 'comment']