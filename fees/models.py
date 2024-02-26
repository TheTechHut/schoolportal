from django.db import models

# Create your models here.

class Fees(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    paid = models.BooleanField()
    date_paid = models.DateTimeField()


    def __str__(self):
        return self.name
