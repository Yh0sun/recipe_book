from django import forms
from .models import Recipe


class RecipeForm(forms.Form):
    # author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # food_name = models.CharField(max_length=500)
    # ingredient = models.TextField()
    # recipe = models.TextField()
    # created_date = models.DateTimeField(default=timezone.now)
    food_name = forms.CharField()
    ingredient = forms.Textarea()
    recipe = forms.Textarea()