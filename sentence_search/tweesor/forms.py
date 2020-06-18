from django import forms
from .models import Label

class IndexForm(forms.ModelForm):   
    label_name = forms.CharField(label='種別',required=False)
    labels = forms.ModelChoiceField(queryset=Label.objects.all(), label='種別')

    class Meta:
        model = Label
        fields = ('label_name','labels')

class SearchForm(forms.Form):
    search = forms.CharField(label='検索')
    class Meta:
        fields = ("search", ) 
