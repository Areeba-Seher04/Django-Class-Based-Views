from django.db import models

class Author(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	date_of_birth = models.DateField(null=True, blank=True,help_text='YYYY-MM-D')
	date_of_death = models.DateField('died', null=True, blank=True,help_text='YYYY-MM-D')

	def __str__(self):
		return self.first_name + ',' + self.last_name