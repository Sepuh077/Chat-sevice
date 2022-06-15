from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'input-field'
            }
        )
    )
    password2 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password confirmation',
                'class': 'input-field'
            }
        )
    )
    
    day = forms.ChoiceField(
        choices=[(i, i) for i in range(1, 32)]
    )
    
    class Meta:
        model = Profile
        
        fields = ['email', 'name', 'birth_date', 'password1', 'password2']
        
        widgets = {
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'E-mail',
                    'class': 'input-field',
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Name surname',
                    'class': 'input-field',
                }
            ),
            'birth_date': forms.DateInput(
                attrs={
                    'placeholder': 'Birth day',
                    'class': 'input-field',      
                }
            ),
        }


class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'E-mail',
                'class': 'input-field',
            }
        )
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'input-field',
            }
        )
    )
