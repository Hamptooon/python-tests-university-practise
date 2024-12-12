from django.test import TestCase
from ..models import Recipe, Ingredient, Unit


class TestContent(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Создание тестовых данных для контента."""
        # Создание единицы измерения
        unit1 = Unit.objects.create(name="Ложка", gram_equivalent=15.0)
        unit2 = Unit.objects.create(name="Стакан", gram_equivalent=250.0)

        # Создание ингредиентов
        ingredient1 = Ingredient.objects.create(name="Сахар", raw_weight=100, cost=10.0, unit=unit1)
        ingredient2 = Ingredient.objects.create(name="Мука", raw_weight=200, cost=20.0, unit=unit2)

        # Создание рецепта
        recipe = Recipe.objects.create(name="Тесто")
        recipe.ingredients.add(ingredient1, ingredient2)

    def test_create_ingredient(self):
        """Проверка создания объекта ингредиента с правильными аттрибутами."""
        ingredient = Ingredient.objects.get(name="Сахар")
        self.assertEqual(ingredient.name, "Сахар")
        self.assertEqual(ingredient.raw_weight, 100)
        self.assertEqual(ingredient.unit.name, "Ложка")

    def test_calculate_weight_in_grams(self):
        """Проверка расчета веса блюда с учетом разных единиц измерения."""
        recipe = Recipe.objects.get(name="Тесто")
        ingredient1 = recipe.ingredients.get(name="Сахар")
        ingredient2 = recipe.ingredients.get(name="Мука")

        # Проверка веса с учетом порции в 1
        self.assertEqual(recipe.calc_weight(raw=True), 100 + 200)  # 100 г (Сахар) + 200 г (Мука)

        # Проверка веса с учетом ложек и стаканов
        self.assertEqual(ingredient1.convert_to_grams(1), 15.0)  # 1 ложка сахара = 15 г
        self.assertEqual(ingredient2.convert_to_grams(1), 250.0)  # 1 стакан муки = 250 г

    def test_recipe_ordering_alphabetically(self):
        """Проверка правильности сортировки рецептов по алфавиту."""
        recipe2 = Recipe.objects.create(name="Пирог")
        recipe3 = Recipe.objects.create(name="Кекс")

        recipes = Recipe.objects.all().order_by('name')
        self.assertEqual([recipe.name for recipe in recipes], ["Кекс", "Пирог", "Тесто"])
