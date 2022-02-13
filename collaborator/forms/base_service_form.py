from django import forms
from phonenumber_field.formfields import PhoneNumberField

PHONE_NUMBER_LENGTH = 10
MIN_AMOUNT_VALUE = 10


class BaseServiceForm(forms.Form):
    client_whatsapp = PhoneNumberField(
        label='Whatsapp del cliente',
        region='MX',
        max_length=PHONE_NUMBER_LENGTH,
        min_length=PHONE_NUMBER_LENGTH,
    )
    amount_to_pay = forms.FloatField(label='Monto del recibo', min_value=MIN_AMOUNT_VALUE)
