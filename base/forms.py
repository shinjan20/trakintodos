from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm,SetPasswordForm
from .models import Todo,User


class resetpasswordform(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
         'id':'id_email',
         'placeholder':'email address'
        })

class setpasswordform(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs.update({
         'id':'id_new_password1',
         'placeholder':'Password',
        })
        self.fields['new_password2'].widget.attrs.update({
         'id':'id_new_password2',
         'placeholder':'Confirm password',
        })

class todoform(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'name':'title',
            'id':'title',
            'placeholder':'Title',
        })
        self.fields['description'].widget.attrs.update({
            'name':'description',
            'id':'description',
            'placeholder':'Explain your task here(Optional).'
        })
        self.fields['is_completed'].widget.attrs.update({
            'id':'is_completed',
        })
    class Meta:
        model = Todo
        exclude = ['user']

class registrationform(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'name':'username',
            'id':'username',
            'placeholder':'username',
            'type' : 'text'
        })
        self.fields['email'].widget.attrs.update({
            'name':'email',
            'id':'email address',
            'placeholder':'email address',
            'type' : 'email'
        })
        self.fields['password1'].widget.attrs.update({
            'id':'password',
            'placeholder':'password',
            'minLength': 8,
            'type' : 'password'
        })
        self.fields['password2'].widget.attrs.update({
            'id':'confirm password',
            'placeholder':'confirm password',
            'minLength': 8,
            'type' : 'password'
        })
    class Meta:
        model = User
        fields = ['username','email','password1','password2']