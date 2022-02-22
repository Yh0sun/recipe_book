from django.shortcuts import render
from django.utils import timezone
from .models import Recipe


def recipe_list(request):
    recipes = Recipe.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'recipe/recipe_list.html', {'recipes':recipes})
