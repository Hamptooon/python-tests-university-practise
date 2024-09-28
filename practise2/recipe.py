# (К)арачев -> (К)артофель по-деревенски
# (И)горь -> (И)ндейка запеченная

from typing import List, Tuple
from pydantic import BaseModel, Field

class Ingredient(BaseModel):
    """Ингредиент."""
    name: str
    raw_weight: float = Field(gt=0)
    cooked_weight: float = Field(gt=0)
    cost: float = Field(ge=0)
    cooking_time: int = Field(ge=0)

    def __str__(self) -> str:
        return f"{self.name} ({self.raw_weight:.0f}г)"

class Receipt:
    def __init__(self, name: str, ingredient_list: List[Tuple[str, float, float, float, int]]) -> None:
        self.name = name
        self.ingredients = [Ingredient(name=ing[0], raw_weight=ing[1], cooked_weight=ing[2], cost=ing[3], cooking_time=ing[4]) for ing in ingredient_list]

    def calc_cost(self, portions=1) -> float:
        return sum(ing.cost * portions for ing in self.ingredients)

    def calc_weight(self, portions=1, raw=True) -> float:
        if raw:
            return sum(ing.raw_weight * portions for ing in self.ingredients)
        else:
            return sum(ing.cooked_weight * portions for ing in self.ingredients)

    def calc_cooking_time(self) -> int:
        return max(ing.cooking_time for ing in self.ingredients)

    def __str__(self) -> str:
        return f"{self.name}\nИнгредиенты:\n" + "\n".join(str(ing) for ing in self.ingredients)

# Данные рецептов
potato_receipt_data = {
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

turkey_receipt_data = {
    "title": "Индейка запеченная",
    "ingredients_list": [
        ('Индейка', 2000, 1600, 500, 120),
        ('Масло сливочное', 100, 80, 80, 0),
        ('Чеснок', 30, 25, 15, 5),
        ('Розмарин', 10, 10, 20, 0),
        ('Тимьян', 10, 10, 20, 0),
        ('Соль', 20, 20, 10, 0),
        ('Перец черный', 10, 10, 15, 0),
    ],
}




#C:\Users\karac\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts\coverage.exe run -m unittest test_recipe.py
#C:\Users\karac\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts\coverage.exe report -m