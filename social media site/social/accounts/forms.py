from django.contrib.auth import get_user_model  # to get the built in user model here to use in forms
from django.contrib.auth.forms import UserCreationForm # we are using inbuilt django's user forms
class UserCreateForm(UserCreationForm):
    class Meta:
        fields=('username','email','password1','password2')   #all fields already in built in user model
        model=get_user_model()
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label='Account Handle'   # this means we want to customize built in username to be shown as account handle
        self.fields['email'].label='Emain Address'