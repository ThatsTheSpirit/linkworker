from django import forms


class UrlForm(forms.Form):
    full_url = forms.URLField(label='URL:', widget=forms.URLInput(
        attrs={'class': 'form-control mb-2', 'for': 'inlineFormInput', 'placeholder': 'Type your link here...'}))
    is_temp = forms.BooleanField(label='Is temp?', required=False, widget=forms.CheckboxInput(
        attrs={'class': 'form-check-input', 'id': 'autoSizingCheck'}))
    # expiration_date = forms.DateField(label='Expiration date:')
