
from django.db import models
from django.utils import timezone


class Recipe(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    food_name = models.CharField(max_length=500)
    ingredient = models.TextField()
    recipe = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.food_name

