from django.db import models

class Ingredient(models.Model):
    """Ингредиент."""
    name = models.CharField(max_length=100)
    raw_weight = models.FloatField(help_text="Вес сырого ингредиента в граммах")
    cooked_weight = models.FloatField(help_text="Вес приготовленного ингредиента в граммах", null=True, blank=True)
    cost = models.DecimalField(max_digits=7, decimal_places=2, help_text="Стоимость ингредиента в рублях")
    cooking_time = models.IntegerField(help_text="Время приготовления в минутах", null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.raw_weight:.0f}г)"


class Recipe(models.Model):
    """Рецепт, содержащий список ингредиентов."""
    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient, related_name="recipes", through='RecipeIngredient')

    def calc_cost(self, portions=1) -> float:
        """Метод для расчета общей стоимости рецепта."""
        return sum(ingredient.cost * portions for ingredient in self.ingredients.all())

    def calc_weight(self, portions=1, raw=True) -> float:
        """Метод для расчета общего веса рецепта."""
        if raw:
            return sum(ingredient.raw_weight * portions for ingredient in self.ingredients.all())
        return sum((ingredient.cooked_weight or ingredient.raw_weight) * portions for ingredient in self.ingredients.all())

    def calc_cooking_time(self) -> int:
        """Метод для расчета максимального времени приготовления среди всех ингредиентов."""
        return max((ingredient.cooking_time for ingredient in self.ingredients.all()), default=0)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    """Промежуточная модель для связи рецепта и ингредиента с количеством."""
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(help_text="Количество ингредиента в рецепте", default=1)

    def __str__(self):
        return f"{self.recipe.name} - {self.ingredient.name} ({self.quantity})"
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='unique_recipe_ingredient',
            )
        ]