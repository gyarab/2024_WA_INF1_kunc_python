from django import forms

class CommentForm(forms.Form):
    author_name = forms.CharField(max_length=100, required=True)
    content = forms.CharField(widget=forms.Textarea, required=True)


    