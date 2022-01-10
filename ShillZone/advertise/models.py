from django.db import models

# Create your models here.
banner_locations = (
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three")
)


class AdvertiseWithUs(models.Model):
    name = models.CharField(max_length=50, null=True)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=200, null=True)
    banner = models.CharField(max_length=40,
                              choices=banner_locations,
                              default='1'
                              )
    banner_img = models.FileField(upload_to='media/', blank=True, null=True)
    redirection_link = models.URLField()

    def __str__(self):
        return 'Inquiry for Advertisment from ' + self.name
