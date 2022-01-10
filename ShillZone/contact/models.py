from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=200)
    phone = models.BigIntegerField()
    comment = models.TextField(max_length=1000)

    def __str__(self):
        return 'Inquiry from ' + self.name