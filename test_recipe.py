import unittest
from recipe import Ingredient, Receipt

class TestRecipe(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ingredient_data = ('Картофель', 500, 400, 50, 30)
        cls.receipt_data = {
            "title": "Картофель по-деревенски",
            "ingredients_list": [
                ('Картофель', 500, 400, 50, 30),
                ('Масло растительное', 50, 50, 20, 0),
                ('Чеснок', 20, 15, 10, 5),
                ('Розмарин', 5, 5, 15, 0),
                ('Соль', 10, 10, 5, 0),
                ('Перец черный', 5, 5, 10, 0),
            ],
        }

    def setUp(self):
        self.ingredient = Ingredient(name=self.ingredient_data[0],
                                     raw_weight=self.ingredient_data[1],
                                     cooked_weight=self.ingredient_data[2],
                                     cost=self.ingredient_data[3],
                                     cooking_time=self.ingredient_data[4])
        self.receipt = Receipt(self.receipt_data['title'], self.receipt_data['ingredients_list'])

    def test_ingredient_creation(self):
        self.assertEqual(self.ingredient.name, 'Картофель')
        self.assertEqual(self.ingredient.raw_weight, 500)
        self.assertEqual(self.ingredient.cooked_weight, 400)
        self.assertEqual(self.ingredient.cost, 50)
        self.assertEqual(self.ingredient.cooking_time, 30)

    def test_receipt_creation(self):
        self.assertEqual(self.receipt.name, 'Картофель по-деревенски')
        self.assertEqual(len(self.receipt.ingredients), 6)

    def test_calc_cost(self):
        expected_cost = sum(ing[3] for ing in self.receipt_data['ingredients_list'])
        self.assertEqual(self.receipt.calc_cost(), expected_cost)

    def test_calc_weight_raw(self):
        expected_weight = sum(ing[1] for ing in self.receipt_data['ingredients_list'])
        self.assertEqual(self.receipt.calc_weight(raw=True), expected_weight)

    def test_calc_weight_cooked(self):
        expected_weight = sum(ing[2] for ing in self.receipt_data['ingredients_list'])
        self.assertEqual(self.receipt.calc_weight(raw=False), expected_weight)

    def test_calc_cooking_time(self):
        expected_time = max(ing[4] for ing in self.receipt_data['ingredients_list'])
        self.assertEqual(self.receipt.calc_cooking_time(), expected_time)

    def test_str_methods(self):
        self.assertIn('Картофель (500г)', str(self.receipt))
        self.assertEqual(str(self.ingredient), 'Картофель (500г)')

    def tearDown(self):
        del self.ingredient
        del self.receipt

    @classmethod
    def tearDownClass(cls):
        del cls.ingredient_data
        del cls.receipt_data

if __name__ == '__main__':
    unittest.main()