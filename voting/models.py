from django.db import models

# Create your models here.
class Vote(models.Model):
	voter = models.IntegerField()
	candidate = models.IntegerField()
