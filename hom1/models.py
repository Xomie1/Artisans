from django.db import models


class SignUp(models.Model):
    # Basic fields
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # You might want to use Django's authentication system here
    
    # Role field with choices
    ROLE_CHOICES = (
        ('user', 'User'),
        ('artisan', 'Artisan'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    
    # Additional fields for artisan
    address = models.CharField(max_length=200, blank=True, null=True)  # Allow blank and null values
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    profession = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.full_name

class Login(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=20)  # Assuming 'user' or 'artisan' roles

 

class Request(models.Model):
    artisan_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return f'Request from {self.username} for {self.artisan_name}'




class Feedback(models.Model):
    artisan_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)                     
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username  # You can adjust this based on your preference
