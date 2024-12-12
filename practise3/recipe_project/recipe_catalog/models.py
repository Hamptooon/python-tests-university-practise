from django.db import models


class Measure(models.Model):
    """Единица измерения для ингредиентов (граммы, ложки, стаканы и т. д.)."""
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    """Ингредиент."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    # def convert_to_grams(self, quantity: float) -> float:
    #     """Преобразует количество ингредиента в граммы в зависимости от единицы измерения."""
    #     if self.unit:
    #         return quantity * self.unit.gram_equivalent
    #     return self.raw_weight * quantity  # если единица измерения не указана, предполагаем, что это граммы


class Recipe(models.Model):
    """Рецепт, содержащий список ингредиентов."""
    id = models.AutoField(primary_key=True)
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
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    raw_measure_weight = models.FloatField(help_text="Вес единицы сырого ингредиента в граммах", null=True)
    cooked_measure_weight = models.FloatField(help_text="Вес единицы приготовленного ингредиента в граммах", null=True, blank=True)
    cooking_time = models.IntegerField(help_text="Время приготовления ингредиента в минутах", null=True, blank=True)
    quantity = models.FloatField(help_text="Количество ингредиента в рецепте", default=1)
    measure = models.ForeignKey(Measure, on_delete=models.SET_NULL, null=True, blank=True, help_text="Единица измерения ингредиента")
    cost = models.DecimalField(max_digits=7, decimal_places=2, help_text="Стоимость ингредиента в рублях")

    def calc_weight(self, raw=True) -> float:
        """Метод для расчета общего веса рецепта."""
        if raw:
            return self.raw_measure_weight * self.quantity
        return self.cooked_measure_weight * self.quantity

    def __str__(self):
        return f"{self.recipe.name} - {self.ingredient.name} ({self.quantity} {self.ingredient.unit.name})"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='unique_recipe_ingredient',
            )
        ]

    # def convert_to_grams(self) -> float:
    #     """Преобразует количество ингредиента в граммы с учетом единицы измерения."""
    #     return self.ingredient.convert_to_grams(self.quantity)
