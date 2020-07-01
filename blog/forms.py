from django.forms import ModelForm, TextInput, Textarea

from blog.models import Comment, Reply


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')
        widgets = {
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name',
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Contents',
            }),
        }
        labels = {
            'author': '',
            'text': '',
        }


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ('author', 'text')
        widgets = {
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name',
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Reply',
            }),
        }
        labels = {
            'author': '',
            'text': '',
        }
