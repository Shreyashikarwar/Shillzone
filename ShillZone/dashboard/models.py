import django
from django.db import models

# Create your models here.


class CreateNewPage(models.Model):
    page_name = models.CharField(max_length=200, null=True, db_column='page name')
    coin_name = models.CharField(max_length=100, null=True, db_column='coin name')
    coin_logo = models.ImageField(upload_to='media/coin_logo/', blank=True, null=True)
    created_by = models.CharField(max_length=200, null=True, )
    created_dt = models.DateTimeField(auto_now=True, db_column='Created Date')

    def __str__(self):
        return 'Coin name ' + self.coin_name + 'is Created'

    class Meta:
        verbose_name_plural = "Coin Page"  # display table name for admin
        db_table = 'coin_page'