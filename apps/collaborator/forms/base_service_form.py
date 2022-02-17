from django import forms
from phonenumber_field.formfields import PhoneNumberField

PHONE_NUMBER_LENGTH = 10
MIN_AMOUNT_VALUE = 10
DECIMAL_PLACES = 2


class BaseServiceForm(forms.Form):
    client_whatsapp = PhoneNumberField(
        label='Whatsapp del cliente',
        region='MX',
        required=False,
    )
    service_discount = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
    )
    amount_to_pay = forms.DecimalField(
        label='Monto del recibo',
        min_value=MIN_AMOUNT_VALUE,
        decimal_places=DECIMAL_PLACES,
        required=True,
    )
