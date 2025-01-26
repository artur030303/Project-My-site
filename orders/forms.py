
from django import forms


# класс формы CreateOrderForm, который наследуется от forms.Form. Этот класс используется для создания HTML-форм, их валидации и обработки данных, введенных пользователем
class CreateOrderForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
  
    # метод  для валидации номера телефона
    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]# получаем значение поле "phone_number" из словаря cleaned_data
        if not phone_number.isdigit():# проверяем, что значение phone_number состоит только из цифр
            raise forms.ValidationError("Номер телефона должен состоять только из цифр")# если значение не является цифрами, то вызываем ValidationError
        if len(phone_number) != 9: # проверяем, что длина номера телефона равна 9
            raise forms.ValidationError("Номер теефона должен состоять из 9 цифр")# если номер телефона не равен 9 цифрам, то вызываем ValidationError

        return phone_number
