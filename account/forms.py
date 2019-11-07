from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate #this authenticate checks user if their cridential is valid or not
from .models import Account


class RegistrationForm(UserCreationForm):
    email               = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')


    class Meta:
        model = Account

        # telling the registration form that what form might looks like
        fields = ("email", "username", "password1", "password2")


class AccountAuthenticationForm(forms.ModelForm):
    password                = forms.CharField(label='Password', widget=forms.PasswordInput) #star typing passwords

    class Meta:
        model = Account                 # what kind of fields is it expecting to see
        fields = ('email', 'password')  # which fields are gonna be visible

    def clean(self):                    # this function is available to any form that extends the model form
            # this method is like a interceptor that means :
                    # that before the form can do anything it has to run this clean method and any logic that we write
                    # in this clean method
            # with this we are going to authenticate user if it's valid or not
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("نام کاربری یا پسور اشتباه می باشد.")


