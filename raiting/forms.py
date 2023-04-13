from django.db import models
from django import forms
from django.forms import ModelForm, TextInput, EmailInput
from captcha.fields import ReCaptchaField
from .models import *


class ContactForm(ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = ContUs
        fields = ['name', 'email', 'message']
        widgets = {
            'name': TextInput(attrs={
                'type':"text",
                'class':"form-control",
                'placeholder':"name",
                'aria-describedby':"basic-addon1"
            }),
            'email': EmailInput(attrs={
                'type':"email",
                'class':"form-control",
                'placeholder':"Email",
                'aria-describedby':"basic-addon2"
            }),
            'message': TextInput(attrs={
                'type':"textarea",
                'class':"form-control",
                'aria-label':"With textarea"
            }),
        }


class reviewForm(ModelForm):
    class Meta:
        model = ReviewUs
        fields = ['message', 'stars']
        exclude = ['user', 'date_created']


