from django import forms
import re
from django.contrib.auth.forms import UserCreationForm
from .models import Diary
from django.contrib.auth import get_user_model


User = get_user_model()

class RegisterForm(UserCreationForm):
    username = forms.CharField(min_length=5, max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control middle', 'id':'username'}))
    full_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control middle', 'id':'f_name'}))
    password1 = forms.CharField(max_length=255, widget = forms.PasswordInput(attrs={'class':'form-control middle', 'id':'password1'}))
    password2 = forms.CharField(max_length=255, widget = forms.PasswordInput(attrs={'class':'form-control middle', 'id':'password2'}))
    #password equalizer
    def clean(self):
        cleaned_data = super().clean()
        
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('password2')
        
        if p2 != p1:
            raise forms.ValidationError("Password doesn't match")   
    
    class Meta:
        model = User
        fields = ('username', 'full_name')

class DiaryForm(forms.ModelForm):
    title = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'middle col-12', 'id':'title','placeholder':'Title','autocapitalize':'word'}))
    diary = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'id':'diary', 'autocapitalize':'sentence'}))
    
    class Meta:
        model = Diary
        fields = ('user', 'title', 'diary', 'img',)