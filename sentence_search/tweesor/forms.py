from django import forms
from .models import Label

class IndexForm(forms.ModelForm):   
    create_label = forms.CharField(label='種別',required=False)

    labels = forms.ModelChoiceField(Label.objects, label='種別',
                                     empty_label='種別を選択してください',
                                     required=False,
                                     widget=forms.Select(attrs={'class':'custom-select'}),
                                     to_field_name='label_mark',
                                     )

    class Meta:
        model = Label
        fields = ('create_label','labels')

class SearchForm(forms.Form):
    search = forms.CharField(label='検索')
    class Meta:
        fields = ("search", ) 
