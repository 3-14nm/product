from django import forms

from django.contrib.auth.models import User

from django.forms import ModelForm, TextInput

from .models import Task, Aim


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['title']


class AimForm(ModelForm):

    class Meta:
        model = Aim
        fields = ['title', 'description', 'date', 'taskAim','taskCur']

# class AimForm(ModelForm):
#
#     class Meta:
#         model = Aim
#         fields = ['title', 'description', 'date']

# class LoginForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].label = "Логин"
#         self.fields['password'].label = "Пароль"
#
#     def clean(self):
#         username = self.cleaned_data['username']
#         password = self.cleaned_data['password']
#         if not User.objects.filtser(username=username).exists():
#             raise forms.ValidationError(f'do not exist')
#         user = User.objects.filter(username=username).first
#
#         if user:
#             if not user.check_password(password):
#                 raise forms.ValidationError(f'incorrect password')
#
#         return self.clean_data



