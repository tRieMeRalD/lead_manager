from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Lead(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100, unique = True) # No repeats
    message = models.CharField(max_length = 500, blank = True) # Optional
    created_at = models.DateTimeField(auto_now_add = True) # Add date automatically
    
    # delete all values related to users and allow null values
    owner = models.ForeignKey(User, related_name="leads", on_delete=models.CASCADE, null=True)