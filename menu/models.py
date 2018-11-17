from django.db import models

# Create your models here.


class MenuItem(models.Model):
	name = models.CharField(max_length=120)
	category = models.CharField(
		max_length=120,
		choices=[('Drink', 'Drink'), ('Food', 'Food')])
	description = models.TextField()
	price = models.DecimalField(decimal_places=0, max_digits=1000)
	featured = models.BooleanField(default=False)
	image = models.ImageField(default='default.png')

	def __str__(self):
		return self.name
