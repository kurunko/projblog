from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import CustomUser
from topics.models import ThreadComment


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    checkBox = forms.BooleanField(required = True, label='Li e estou de acordo com os Termos de Uso da Ongame Entretenimento®..',)


    class Meta:
        model = CustomUser
        fields = (
        'email',

    )

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CustomUserChangeForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class UserUpdateForm(forms.ModelForm):
    """
        Creates form for user to update their account.
    """


    class Meta:
        model = CustomUser
        fields = ['firstName', 'lastName', 'gender', 'birthDate', 'image']
        widgets = {

            'firstName': forms.TextInput(attrs={
                'name': "first-name",
                'class': "form-control",
                'id': "first-name"
            }),

            'lastName': forms.TextInput(attrs={
                'name': "last-name",
                'class': "form-control",
                'id': "last-name"
            }),
        }


class FlagAsSpamForm(forms.ModelForm):

    class Meta:
        model = ThreadComment
        fields = (
        'flagged',
        'reason'

    )