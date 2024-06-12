from django import forms
from .models import Comment, Post
 
class CommentForm(forms.ModelForm):
    content = forms.CharField(label ="", widget = forms.Textarea(
    attrs ={
        'class':'form-control',
        'placeholder':'Comment here !',
        'rows':4,
        'cols':50
    }))
    class Meta:
        model = Comment
        fields =['content']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'caption']
        widgets = {
            'title': forms.TextInput(
                attrs ={
                    'class': 'form-control',
                    'placeholder':'Enter post title here !'
                }),
            'caption': forms.Textarea(
                attrs ={
                    'class': 'form-control', 
                    'placeholder':'Enter the post caption here !',
                    'rows': 4
                }),
        }