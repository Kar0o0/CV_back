from django import forms
from django.core import validators
from .models import Contact

class ContactModelForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name','email','subject','message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control col-md-12',
                'placeholder' : 'نام شما',
                'width':'100%',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control col-md-12',
                'placeholder': 'ایمیل شما',

            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control col-md-12',
                'placeholder': 'موضوع پیام شما',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control col-md-12',
                'placeholder': '...',
                'rows': 5,
                'cols':10,
                'id': 'message'
            })
        }

        labels = {
            'name': 'نام و نام خانوادگی شما',
            'email': 'ایمیل شما',
            'subject':'موضوع پیام',
            'message':'متن پیام'
        }

        error_messages = {
            'full_name': {
                'required': 'لطفا نام و نام خانوادگی خود را وارد کنید'
            },
            'email':{
                'required':'لطفا آدرس ایمیل خود را وارد کنید'
            },
            'subject':{
                'required' : 'لطفا موضوع پیام خود را وارد کنید'
            },
            'message':{
                'required': 'لطفا پیام خود را وارد کنید'
            }
        }