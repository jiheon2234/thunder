from django import forms
from .models import *

class GoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields =[ 'name', 'is_new', 'desc'
                , 'can_change', 'where', 'price'
                ,'already_sell']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
