from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Record
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1']
        widgets = {
            
        }


class UpdateRecordForm(ModelForm):
    class Meta:
        model = Record
        fields = "__all__"
        widgets = {
            
        }