from django.db import models

class User(models.Model):
    Date = models.CharField(max_length=50)
    Month = models.CharField(max_length=30)
    def __str__ (self):
        return self.Date+' '+self.Month