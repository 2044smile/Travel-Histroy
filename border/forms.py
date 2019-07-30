from django import forms
from .models import Border

class BorderForm(forms.ModelForm):

    class Meta: # Form 을 만들기 위해서 어떤 model 이 쓰여야되는지
        model = Border
        fields = ('title','author','text','photo')