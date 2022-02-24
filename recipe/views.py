from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import RecipeForm
from .models import Recipe


def recipe_list(request):
    recipes = Recipe.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'recipe/recipe_list.html', {'recipes': recipes})


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe/recipe_detail.html', {'recipe': recipe})


def recipe_new(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            cleaned_data_dict = form.cleaned_data
            recipe = Recipe.objects.create(
                author=request.user,
                food_name=cleaned_data_dict['food_name'],
                ingredient=cleaned_data_dict['ingredient'],
                recipe=cleaned_data_dict['recipe'],
                created_date=timezone.now()
            )
            return redirect('recipe_detail', pk=recipe.pk)
        else:
            form = RecipeForm()
        return render(request, 'recipe/recipe_edit.html', {'recipeForm': form})


def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.published_date = timezone.now()
            recipe.save()
            return redirect('recipe_edit', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipe/recipe_edit.html', {'recipeForm': form})
