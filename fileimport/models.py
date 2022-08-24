from django.db import models

# Create your models here.
class Question (models.Model):
    previous_year = models.CharField(max_length =400)
    level = models.CharField(max_length = 10)
    question = models.CharField(max_length = 2000)
    option1 = models.CharField( max_length=500) 
    option2 = models.CharField( max_length=500) 
    option3 = models.CharField( max_length=500) 
    option4 = models.CharField( max_length=500)
    explanation = models.CharField(max_length = 1000)
    answer = models.IntegerField()    