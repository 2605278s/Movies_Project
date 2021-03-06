from django import forms
from django.forms.widgets import HiddenInput
from rango.models import ContactUs, Page, Category
from django.contrib.auth.models import User
from rango.models import UserProfile

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                            help_text="Please enter category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200,
                        help_text="Please enter the title of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page

        exclude = ('category',)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url

        return cleaned_data

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class']='form-control'    

                

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone',)
            
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class']='form-control'  
        


class ContactUsForm(forms.ModelForm):
    name = forms.CharField(max_length=ContactUs.NAME_MAX_LENGTH, help_text="Name",)
    subject = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write Something'}), max_length=ContactUs.SUBJECT_MAX_LENGTH, help_text="Subject",  )

    class Meta:
        model = ContactUs
        fields = ('name','subject')

class ReviewForm(forms.ModelForm):
    title = forms.CharField(max_length=ContactUs.NAME_MAX_LENGTH, help_text="Title",)
    review = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write Something'}), max_length=ContactUs.SUBJECT_MAX_LENGTH, help_text="Review",  )
    film = forms.CharField(max_length=ContactUs.NAME_MAX_LENGTH, help_text= 'Film')

    class Meta:
        model = ContactUs
        fields = ('title','review','film')

