from django import forms
from django.contrib.auth.models import User
from users.models import Profile


class ProfileForm(forms.ModelForm):
    
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, 
        widget=forms.PasswordInput()
        )
    username = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.CharField(max_length=30)
    

    # def __init__(self, *args, **kwargs):
    #     super(ProfileForm, self).__init__(*args, **kwargs)
    #     self.fields['first_name'].initial = self.instance.user.first_name
    #     self.fields['last_name'].initial = self.instance.user.last_name
    #     self.fields['username'].initial = self.instance.user.username
    #     self.fields['password'].initial = self.instance.user.password
    #     self.fields['email'].initial = self.instance.user.email

        # self.fields.keyOrder = [
        #     'first_name',
        #     'last_name',
        #     'username',
        #     'password',
        #     'email'
        #     ]

    def save(self, *args, **kwargs):
        super(ProfileForm, self).save(*args, **kwargs)
        self.instance.user.first_name = self.cleaned_data.get('first_name')
        self.instance.user.last_name = self.cleaned_data.get('last_name')
        self.instance.user.username = self.cleaned_data.get('username')
        self.instance.user.password = self.cleaned_data.get('password')
        self.instance.user.email = self.cleaned_data.get('email')
        self.instance.user.save()

    class Meta:
        model = Profile
        fields = [
            'username','password', 'email', 
            'first_name', 'last_name',
            'phone_number'
        ]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username','email',
            'first_name', 'last_name'
            ]
class ChangePhoneForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'phone_number',
            ]