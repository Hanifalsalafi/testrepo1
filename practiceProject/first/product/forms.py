from django.core import validators
from django import forms

class RecentProduct(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    retype_password = forms.CharField(widget=forms.PasswordInput) #mobile attribute work as like html label
    laptop = forms.CharField(label='Enter Your laptop Name') #Form Field argument, Form Widget
    email = forms.EmailField(label='Enter your email address',label_suffix=' = ',validators=[validators.MaxLengthValidator(30)])
    about = forms.CharField(help_text='Describe about you')
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':4,'cols':40}))
    checkbox = forms.CharField(widget=forms.CheckboxInput )
    files = forms.CharField(widget=forms.FileInput)
    ram = forms.IntegerField(min_value=4, max_value=12)
    ssd = forms.DecimalField(min_value=1, max_value=40, max_digits=3, decimal_places=2)
    youtube_channal=forms.BooleanField(label='subscribe the channal') # for custom validation
    
    def clean(self) :
        clean_data = super().clean()
        password_match = self.clean_data ['password']
        retype_password_match = self.clean_data['retype_password']
        if password_match != retype_password_match :
            raise forms.ValidationError("Password dosen't match")