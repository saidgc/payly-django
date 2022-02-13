from phonenumber_field.formfields import PhoneNumberField

from collaborator.forms.base_service_form import BaseServiceForm

PHONE_NUMBER_LENGTH = 10


class TelmexForm(BaseServiceForm):
    telmex_number = PhoneNumberField(
        label='Número Telmex del cliente',
        region='MX',
        max_length=PHONE_NUMBER_LENGTH,
        min_length=PHONE_NUMBER_LENGTH,
    )

    field_order = ['client_whatsapp', 'telmex_number', 'amount_to_pay']
