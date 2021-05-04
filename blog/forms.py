from .models import Comments
from django import forms


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'comment here ...',
        'rows': 4,
        'cols': 50
    }))

    class Meta:
        model = Comments
        fields = ['content']
