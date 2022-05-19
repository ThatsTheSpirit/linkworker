from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UrlForm(forms.Form):
    full_url = forms.URLField(label='URL:', widget=forms.URLInput(
        attrs={'class': 'form-control mb-2', 'for': 'inlineFormInput', 'placeholder': 'Введите вашу ссылку...'}))
    is_temp = forms.BooleanField(label='Сделать временной?', required=False, widget=forms.CheckboxInput(
        attrs={'class': 'form-check-input', 'id': 'autoSizingCheck'}))
    # expiration_date = forms.DateField(label='Expiration date:')
