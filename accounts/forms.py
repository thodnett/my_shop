from django import forms

class UserLoginForm(forms.Form):
    """Form to be used to log in user"""
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    

