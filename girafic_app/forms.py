from django import forms
from girafic_app.models import Review, ClientData, BoxOrder, DreamcatcherOrder, LetterOrder
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    username = forms.CharField(label='Имя пользователя')
    # email
    # first_name
    # last_name
    class Meta:
        model = User
        fields = ('username','password', 'email','first_name','last_name')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text', )

# from django.core import validators
#
# def start_with_a(value):
#     if value[0].lower() != 'a':
#         raise forms.ValidationError('Значение должно начинаться с буквы "а"')

class SomeForm(forms.Form):
    name = forms.CharField()#validators=[start_with_a])
    mail = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)#, validators=[validators.MaxLengthValidator(5)])
    password = forms.CharField(widget=forms.PasswordInput, label='Введите пароль')
    password_double = forms.CharField(widget=forms.PasswordInput, label='Введите пароль ещё раз')

    def clean(self):
        cleaned_data = super().clean()
        passw = cleaned_data['password']
        passw_doub = cleaned_data['password_double']
        if passw != passw_doub:
            raise forms.ValidationError('Пароли не совпадают')
        return cleaned_data

class ClientDataForm(forms.ModelForm):
    class Meta:
        model = ClientData
        fields = ('fullname', 'post_address', 'phone')

class BoxOrderForm(forms.ModelForm):
    name = forms.CharField(widget=forms.HiddenInput, required=False)
    class Meta:
        model = BoxOrder
        fields = ('lenght', 'width', 'height', 'name')

class DreamcatcherOrderForm(forms.ModelForm):
    name = forms.CharField(widget=forms.HiddenInput, required=False)
    class Meta:
        model = DreamcatcherOrder
        fields = ('diameter', 'name')

class LetterOrderForm(forms.ModelForm):
    name = forms.CharField(widget=forms.HiddenInput, required=False)
    class Meta:
        model = LetterOrder
        fields = ('lenght', 'width', 'color', 'name')
