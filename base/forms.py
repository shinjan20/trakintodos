from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Todo

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
            'placeholder':'Explain your task here.'
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
        fields = ['username','password1','password2']