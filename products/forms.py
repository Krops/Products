from django.forms import CharField, Form
from django.forms import TextInput, PasswordInput

class LoginForm(Form):
    myatr = {'style': 'width:100%'}
    username = CharField(max_length=30, required=True,
                         widget=TextInput(attrs=myatr))
    password = CharField(max_length=30, required=True,
                         widget=PasswordInput(attrs=myatr))
