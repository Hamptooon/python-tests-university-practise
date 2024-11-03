from django.shortcuts import render, get_object_or_404
from .models import Recipe

def about(request):
    return render(request, 'recipe_catalog/about.html')

def index(request):
    recipes = Recipe.objects.all()
    return render(
        request=request,
        template_name='recipe_catalog/index.html',
        context={'recipes': recipes}
    )

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    total_raw_weight = recipe.calc_weight(raw=True)
    total_cooked_weight = recipe.calc_weight(raw=False)
    return render(
        request=request,
        template_name='recipe_catalog/recipe.html',
        context={
            'recipe': recipe,
            'total_raw_weight': total_raw_weight,
            'total_cooked_weight': total_cooked_weight,
        }
    )
