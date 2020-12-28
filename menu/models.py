from django.db import models

# Create your models here.
class Menu(models.Model):
	item = models.CharField(max_length = 64)
	price = models.IntegerField()
	code = models.CharField(max_length = 3)

	def __str__(self):
		return f"{self.code} : {self.item} costing {self.price} rs. "


class order(models.Model):
	name = models.CharField(max_length = 64)
	order = models.ForeignKey(Menu, on_delete = models.CASCADE)
	#addition = models.ForeignKey(topping, on_delete = models.CASCADE)

	def __str__(self):
			return f"{self.name} ordered : {self.order.item}  "


#with topping : {self.addition.name}