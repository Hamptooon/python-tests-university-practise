import unittest
from recipe import Ingredient, Receipt, potato_receipt_data, turkey_receipt_data

class TestRecipe(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.potato_receipt_data = potato_receipt_data
        cls.turkey_receipt_data = turkey_receipt_data

    def setUp(self):
        self.potato_receipt = Receipt(self.potato_receipt_data['title'], self.potato_receipt_data['ingredients_list'])
        self.turkey_receipt = Receipt(self.turkey_receipt_data['title'], self.turkey_receipt_data['ingredients_list'])

    def test_ingredient_creation(self):
        ingredient = Ingredient(name='Картофель', raw_weight=500, cooked_weight=400, cost=50, cooking_time=30)
        self.assertEqual(ingredient.name, 'Картофель')
        self.assertEqual(ingredient.raw_weight, 500)
        self.assertEqual(ingredient.cooked_weight, 400)
        self.assertEqual(ingredient.cost, 50)
        self.assertEqual(ingredient.cooking_time, 30)

    def test_receipt_creation(self):
        self.assertEqual(self.potato_receipt.name, 'Картофель по-деревенски')
        self.assertEqual(len(self.potato_receipt.ingredients), 6)
        self.assertEqual(self.turkey_receipt.name, 'Индейка запеченная')
        self.assertEqual(len(self.turkey_receipt.ingredients), 7)

    def test_calc_cost(self):
        expected_potato_cost = sum(ing[3] for ing in self.potato_receipt_data['ingredients_list'])
        expected_turkey_cost = sum(ing[3] for ing in self.turkey_receipt_data['ingredients_list'])
        self.assertEqual(self.potato_receipt.calc_cost(), expected_potato_cost)
        self.assertEqual(self.turkey_receipt.calc_cost(), expected_turkey_cost)

    def test_calc_weight_raw(self):
        expected_potato_weight = sum(ing[1] for ing in self.potato_receipt_data['ingredients_list'])
        expected_turkey_weight = sum(ing[1] for ing in self.turkey_receipt_data['ingredients_list'])
        self.assertEqual(self.potato_receipt.calc_weight(raw=True), expected_potato_weight)
        self.assertEqual(self.turkey_receipt.calc_weight(raw=True), expected_turkey_weight)

    def test_calc_weight_cooked(self):
        expected_potato_weight = sum(ing[2] for ing in self.potato_receipt_data['ingredients_list'])
        expected_turkey_weight = sum(ing[2] for ing in self.turkey_receipt_data['ingredients_list'])
        self.assertEqual(self.potato_receipt.calc_weight(raw=False), expected_potato_weight)
        self.assertEqual(self.turkey_receipt.calc_weight(raw=False), expected_turkey_weight)

    def test_calc_cooking_time(self):
        expected_potato_time = max(ing[4] for ing in self.potato_receipt_data['ingredients_list'])
        expected_turkey_time = max(ing[4] for ing in self.turkey_receipt_data['ingredients_list'])
        self.assertEqual(self.potato_receipt.calc_cooking_time(), expected_potato_time)
        self.assertEqual(self.turkey_receipt.calc_cooking_time(), expected_turkey_time)

    def test_str_methods(self):
        self.assertIn('Картофель (500г)', str(self.potato_receipt))
        self.assertIn('Индейка (2000г)', str(self.turkey_receipt))
        ingredient = self.potato_receipt.ingredients[0]
        self.assertEqual(str(ingredient), 'Картофель (500г)')

    def test_portions(self):
        self.assertAlmostEqual(self.potato_receipt.calc_cost(portions=2), self.potato_receipt.calc_cost() * 2)
        self.assertAlmostEqual(self.turkey_receipt.calc_weight(portions=3), self.turkey_receipt.calc_weight() * 3)

    def tearDown(self):
        del self.potato_receipt
        del self.turkey_receipt

    @classmethod
    def tearDownClass(cls):
        del cls.potato_receipt_data
        del cls.turkey_receipt_data

if __name__ == '__main__':
    unittest.main()