from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                             widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class SearchForm(forms.Form):
    choices = (
        ('1', 'body and title(trigramSimilarity)'),
        ('2', 'only title(searchVector)'),
    )
    which_search_engine = forms.ChoiceField(label="Po czym wyszukać?",
                                            choices=choices)
    query = forms.CharField(label="Treść zapytania:",
                            widget=forms.Textarea)

