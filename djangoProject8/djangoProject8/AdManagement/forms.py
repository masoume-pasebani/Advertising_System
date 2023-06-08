from django import forms


class Form(forms.Form):
    advertiser_id = forms.IntegerField()
    Img = forms.ImageField()
    Title = forms.CharField()
    Link = forms.URLField()