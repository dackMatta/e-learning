from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms.models import inlineformset_factory
from .models import Course,Modules



ModuleFormSet=inlineformset_factory(Course,Modules,
                                    fields=['title',
                                            'description'],
                                            extra=2,
                                            can_delete=True)

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')], required=True)
    phone_number = forms.CharField(max_length=15, required=True)

    class Meta:
        model = get_user_model()
        fields = [
           
            'first_name', 'last_name', 'phone_number','date_of_birth',
            'gender', 'email', 'password1', 'password2',
        ]
