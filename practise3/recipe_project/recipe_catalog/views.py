from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import RecipeIngredient
from .forms import RegistrationForm
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
    recipe_ingredients = RecipeIngredient.objects.filter(recipe=recipe)
    ingredients_list = [
        {
            'id': recipe_ingredient.ingredient.id,
            'name': recipe_ingredient.ingredient.name,
            'measure': recipe_ingredient.ingredient.measure.name,
            'raw_measure_weight': recipe_ingredient.raw_measure_weight,
            'cooked_measure_weight': recipe_ingredient.coocked_measure_weight,
            'cooking_time': recipe_ingredient.cooking_time,
            'quantity': recipe_ingredient.quantity,
            'cost': recipe_ingredient.cost,

        }
        for recipe_ingredient in recipe_ingredients
    ]

    total_cost = sum([ingredient['cost'] for ingredient in ingredients_list])
    total_raw_weight = sum([ingredient['raw_measure_weight'] * ingredient['quantity']
                        for ingredient in ingredients_list])
    total_cooked_weight = sum([ingredient['cooked_measure_weight'] * ingredient['quantity']
                            for ingredient in ingredients_list])
    total_cooking_time = sum([ingredient['cooking_time'] for ingredient in ingredients_list])
    context = {
        "recipe": recipe,
        "recipe_ingredients": ingredients_list,
        "total_cost": total_cost,
        "total_raw_weight": total_raw_weight,
        "total_cooked_weight": total_cooked_weight,
        "total_cooking_time": total_cooking_time,
    }
    return render(
        request=request,
        template_name='recipe_catalog/recipe.html',
        context=context
    )
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # Автоматически логиним пользователя после регистрации
            return redirect('index')
    else:
        form = RegistrationForm()

    return render(request, 'recipe_catalog/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse("Неверные учетные данные")
    return render(request, 'recipe_catalog/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')