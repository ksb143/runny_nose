from django import forms 
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        widget=forms.TextInput(
            attrs={
                'class' : 'my-title'
            }
        )
    )

    class Meta:
        model = Article
        fields = '__all__'