from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Post")
    post = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
    	return "{} ".format(self.post)    
    
    
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Comments")
    comments = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
    	return "{} ".format(self.comments) 
 

GENDER_MALE = 'male'
GENDER_FEMALE = 'female'
GENDER_OTHER = 'other'
GENDER_NOT_SPECIFIED = 'not specified'
GENDER_CHOICES = (
    (GENDER_MALE, 'Male'),
    (GENDER_FEMALE, 'Female'),
    (GENDER_OTHER, 'Other'),
    (GENDER_NOT_SPECIFIED, 'Not specified'),
)


class User_Detail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, default='',
                             blank=True, unique=True)
    about_me = models.TextField(blank=True, default='', max_length=10000)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(
        max_length=32, choices=GENDER_CHOICES, default=GENDER_NOT_SPECIFIED)
    profile_picture = models.ImageField(
        blank=True, null=True, upload_to='image')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    
