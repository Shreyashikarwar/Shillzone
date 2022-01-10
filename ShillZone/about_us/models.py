from django.db import models


# Create your models here.

class AboutUs(models.Model):
    about1 = models.TextField(max_length=3000, db_column="about_us_1", null=False)
    about2 = models.TextField(max_length=3000, db_column="about_us_2", null=False)
    image1 = models.ImageField( default='')
    image2 = models.ImageField( default='')

    class Meta:
        verbose_name_plural = "About Us"  # display table name for admin
        db_table = 'about_us'
