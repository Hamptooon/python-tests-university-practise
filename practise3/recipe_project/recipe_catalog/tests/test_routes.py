from django.test import TestCase
from django.urls import reverse
from ..models import Recipe, Ingredient, Unit


class TestRoutes(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Создание тестовых данных для маршрутов."""
        # Создание единицы измерения
        unit = Unit.objects.create(name="Ложка", gram_equivalent=15.0)

        # Создание ингредиентов
        ingredient1 = Ingredient.objects.create(name="Сахар", raw_weight=100, cost=10.0, unit=unit)
        ingredient2 = Ingredient.objects.create(name="Мука", raw_weight=200, cost=20.0, unit=unit)

        # Создание рецепта
        recipe = Recipe.objects.create(name="Тесто")
        recipe.ingredients.add(ingredient1, ingredient2)

    def test_recipe_list_page(self):
        """Тестируем маршрут для списка рецептов."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Тесто")  # Проверка, что рецепт "Тесто" отображается

    def test_recipe_detail_page(self):
        """Тестируем маршрут для деталей рецепта."""
        recipe = Recipe.objects.get(name="Тесто")
        response = self.client.get(reverse('recipe_detail', args=[recipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Тесто")  # Проверка, что рецепт "Тесто" отображается на странице деталей

    def test_about_page(self):
        """Тестируем маршрут для страницы "О каталоге"."""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "О нас")  # Проверка наличия текста "О каталоге" на странице
