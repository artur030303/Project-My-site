from ast import pattern
from django import forms


class CreateOrderForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        if not phone_number.isdigit():
            raise forms.ValidationError("Номер телефона должен состоять только из цифр")
        if len(phone_number) != 10:
            raise forms.ValidationError("Номер теефона должен состоять из 10 цифр")

        return phone_number
