from django.db import models

# Create your models here.
class DataModel(models.Model):
    """Model that contains a JSONField."""
    
    data = models.JSONField()
