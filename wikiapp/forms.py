from django import forms
from wikiapp import models
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(label='名稱', max_length=10)
    password = forms.CharField(label='密碼', widget=forms.PasswordInput())
    captcha = CaptchaField(label='驗證碼', error_messages={"invalid": "驗證碼輸入錯誤"})


