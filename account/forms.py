from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.template.defaultfilters import capfirst
from django import forms

UserModel = get_user_model()


class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

        # Set the max length and label for the "username" field.
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        username_max_length = self.username_field.max_length or 254
        print(self.fields)
        self.fields["username"].max_length = username_max_length
        self.fields["username"].widget.attrs["maxlength"] = username_max_length
        self.fields["username"].widget.attrs["class"] = "form-control shadow-sm mx-10 rounded-pill"
        self.fields["password"].widget.attrs["class"] = "form-control shadow-sm mx-10 rounded-pill"
        if self.fields["username"].label is None:
            self.fields["username"].label = capfirst(self.username_field.verbose_name)


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', required=True)
    first_name = forms.CharField(label='Имя', required=True)
    last_name = forms.CharField(label='Фамилия', required=True)
    surname = forms.CharField(label="Отчество", required=True)
    phone = forms.CharField(label="Телефон", required=True)
    email = forms.EmailField(required=True)

    error_messages = {
        'duplicate_username': "Пользователь с таким именем уже существует",
        'password_mismatch': "Введенные пароли не совпадают",
    }

    field_order = ['username', 'first_name', 'last_name', "surname", "phone", 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields['email'].help_text = 'Введите e-mail'
        self.fields['username'].help_text = 'Может содержать только буквы, цифры и символы @ . + - _'
        self.fields['password1'].help_text = """
        Пароль не может быть похож на имя пользователя.

        Пароль должен содержать как минимум 8 символов.

        Пароль не должен быть простым и часто используемым.

        Пароль не должен содержать только цифры.
        """
        self.fields['password2'].help_text = 'Для подтверждения введите, пожалуйста, пароль ещё раз.'
        self.fields['username'].widget.attrs['maxlength'] = 20
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control shadow-sm p-3 rounded-pill"
        # self.fields['username'].widget.attrs['class'] = 'w-100'
