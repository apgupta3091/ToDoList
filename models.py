from django.db import models

#Class List has var item to set the max character length
#Class completed has var to set the completed default value to False
class List(models.Model):
	item = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)

	def __str__(self):
		return self.item + ' | ' + str(self.completed)
# Create your models here.
