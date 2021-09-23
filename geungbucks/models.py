from django.db import models



class Basket(models.Model): 
    subject = models.CharField(max_length=30)
    price = models.FloatField()
    volume = models.IntegerField()