from django import forms
from news.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegisterform(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=150)
    last_name = forms.CharField(required=True, max_length=150)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))

class NewsForm(forms.ModelForm):
    class Meta:
        model = news
        fields = ['title', 'content', 'thumbnail', 'tags']

        tags = forms.ModelMultipleChoiceField(
            queryset=tags.objects.all(),
            widget=forms.SelectMultiple(attrs={'class': 'form-select'}),
            required=False)


class TagForm(forms.ModelForm):
    class Meta:
        model = tags
        fields = ['name']

class CommentForm(forms.ModelForm):
    class Meta:
        model = comments
        fields = ['comment']