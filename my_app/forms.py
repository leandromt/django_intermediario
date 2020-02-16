from django import forms
from .models import STATE_CHOICE


class AddressForm(forms.Form):
    address = forms.CharField(
        label='Endereço',
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    address_complement = forms.CharField(
        label='Complemento',
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    city = forms.CharField(
        label='Cidade',
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    state = forms.ChoiceField(
        label='Estado',
        choices=STATE_CHOICE,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    country = forms.CharField(
        label='País',
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
