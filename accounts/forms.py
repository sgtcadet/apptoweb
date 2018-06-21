from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    """
    def __init__(self, *args,**kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)
        del self.fields['username']
    """
    class Meta:
        model = CustomUser
        fields = (
            'firstname',
            'lastname',
            'email',
        )


class CustomUserAuthorizationForm(forms.Form):
    """
    model = CustomUser
    fields = (
        'auth_number'
    )"""

    auth_number = forms.CharField(label='Authorization Number', max_length=30)
    email = forms.EmailField(initial='testing', widget=forms.HiddenInput())
