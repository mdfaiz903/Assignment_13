from django.db import models

# Create your models here.
class contact_model(models.Model):
    first_name = models.CharField( max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    content = models.TextField()
    def __str__(self):
        return self.first_name