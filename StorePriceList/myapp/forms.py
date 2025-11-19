from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import Inventory, StoreProfile

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email...', 'autocomplete': 'email'})
    )
    first_name = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name...', 'autocomplete': 'name'})
    )
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove username field from form
        if 'username' in self.fields:
            del self.fields['username']
        # Make email required and set it as the username
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        
        # Style password fields
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control', 
            'placeholder': 'Password...',
            'autocomplete': 'new-password',
            'id': 'id_password1'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control', 
            'placeholder': 'Confirm Password...',
            'autocomplete': 'new-password',
            'id': 'id_password2'
        })
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name:
            first_name = first_name.strip()
            if not first_name:
                raise ValidationError("Enter your full name")
        return first_name
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            email = email.lower().strip()
            if not email:
                raise ValidationError("Enter a valid email address")
            # Email format validation
            import re
            pattern = r'^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$'
            if not re.match(pattern, email, re.IGNORECASE):
                raise ValidationError("Enter a valid email address")
            if User.objects.filter(email=email).exists():
                raise ValidationError("Email already registered")
            if User.objects.filter(username=email).exists():
                raise ValidationError("Email already registered")
        return email
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1 and len(password1) < 6:
            raise ValidationError("Password must be at least 6 characters")
        return password1
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        if password1 and password2:
            if password1 != password2:
                raise ValidationError({'password2': "Passwords do not match"})
        
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        # Use email as username
        email = self.cleaned_data.get('email').lower().strip()
        user.username = email
        user.email = email
        user.first_name = self.cleaned_data.get('first_name')
        if commit:
            user.save()
        return user

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['product_name', 'product_description', 'price']
