__author__ = 'josegregorio'

from django.forms import Form, CharField
from django.forms.widgets import TextInput, PasswordInput


class LoginForm(Form):
    ATTR_DICT = {'class': 'form-control'}
    username = CharField(label='Username', widget=TextInput(attrs=ATTR_DICT))
    password = CharField(label='Password', widget=PasswordInput(attrs=ATTR_DICT))
    error_css_class = 'error'
