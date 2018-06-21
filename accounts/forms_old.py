from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args,**kargs)
        del self.fields['username']

    class Meta:
        model = CustomUser
        fields = ('firstname','lastname','email')


class CustomUserChangeForm(UserChangeForm):

    def __init__(self, *args, **kargs):
        super(CustomUserChangeForm,self).__init__(*args,**kargs)
        del self.fields['username']

    class Meta:
        model = CustomUser
        fields = ('firstname','lastname','email')