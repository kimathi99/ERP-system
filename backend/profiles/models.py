from django.db import models
from accounts.models import User
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError


def validate_pdf(value):
    ext = value.name.split('.')[-1]
    if ext.lower() != 'pdf':
        raise ValidationError("Only PDF files are allowed.")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    bio = models.TextField(blank=True)
    facebook_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    company = models.CharField(max_length=100, blank=True)
    job_title = models.CharField(max_length=100, blank=True)
    work_experience = models.TextField(blank=True)
    education_background = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    interests = models.TextField(blank=True)
    privacy_settings = models.TextField(blank=True)
    cv = models.FileField(upload_to='cv', validators=[FileExtensionValidator(['pdf']), validate_pdf], blank=True)

    def __str__(self):
        return self.user.username
