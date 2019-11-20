from django.db import models
from dateutil.relativedelta import relativedelta


# Create your models here.
class Candidate(models.Model):
	name = models.CharField(max_length=200)
	region = models.IntegerField()
	votes = models.IntegerField()

class Voter(models.Model):
	name = models.CharField(max_length=200)
	region = models.IntegerField()
	address = models.TextField(null=True)
	father_name =models.TextField(null=True)
	dob =models.DateTimeField(blank=True, null=True)
	age=models.IntegerField(null=True)
	def __str__(self):
            today =date.today()
            delta=relativedelta(today,self.dob)
            return str(delta.years)


                    