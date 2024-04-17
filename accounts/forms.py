from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    address = forms.CharField(max_length=255)
    picture = forms.ImageField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'address', 'picture')

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            UserProfile.objects.create(user=user, address=self.cleaned_data['address'], picture=self.cleaned_data['picture'])
        return user
