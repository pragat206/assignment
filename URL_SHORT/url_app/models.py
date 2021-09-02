from django.db import models

# Create your models here.

class UrlData(models.Model):
    url = models.CharField(max_length=100)
    short = models.CharField(max_length=15)

    def __str__(self):
        return "Long URL:{} and Short URL is {}".format(self.url,self.short)
