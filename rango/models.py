from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Category(models.Model):
    NAME_MAX_LENGTH = 128

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    MAX_PHONE_LENGTH = 15
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #website = models.URLField(blank=True)
    #picture = models.ImageField(upload_to='profile_images', blank=True)
    phone = PhoneNumberField(max_length = MAX_PHONE_LENGTH)

    def __str__(self):
        return self.user.username

class ContactUs(models.Model):
    NAME_MAX_LENGTH = 128
    SUBJECT_MAX_LENGTH = 5000
    name =  models.CharField(max_length=NAME_MAX_LENGTH)
    subject = models.CharField(max_length=SUBJECT_MAX_LENGTH)
    class Meta:
        verbose_name_plural = 'Contact us queries'
    def __str__(self):
        return self.name

