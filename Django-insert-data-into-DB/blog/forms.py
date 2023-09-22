from django.forms import ModelForm
from .models import Article

class AtricleModelForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

