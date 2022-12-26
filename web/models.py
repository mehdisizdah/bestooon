from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Expense(models.Model):
    text=models.CharField(max_length=255)
    date=models.DateTimeField()
    amount=models.BigIntegerField()
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    def __str__(self):                                  #__unicode__ kar nakard bar khalafe ammozesh
        return "{} , {}T".format(self.user,self.amount)

class Income(models.Model):
    text=models.CharField(max_length=255)
    date=models.DateTimeField()
    amount=models.BigIntegerField()
    user=models.ForeignKey(User,on_delete=models.RESTRICT)
    def __str__(self):
        return "{} , {}T".format(self.user,self.amount)
