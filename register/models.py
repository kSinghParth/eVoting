from django.db import models

# Create your models here.
class Candidate(models.Model):
	name = models.CharField(max_length=200)
	region = models.IntegerField()

class Voter(models.Model):
	name = models.CharField(max_length=200)
	region = models.IntegerField()

