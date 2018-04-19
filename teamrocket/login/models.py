from django.db import models

class User(models.Model):
	Username = models.CharField(max_length=50)
	Password = models.CharField(max_length=50)

	def __str__(self):
		return self.Username
