# (К)арачев -> (К)артофель по-деревенски

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

if __name__ == '__main__':
    receipt_from_api = {
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

    receipt = Receipt(receipt_from_api['title'], receipt_from_api['ingredients_list'])

    print(receipt)
    print(f"Стоимость: {receipt.calc_cost():.2f} руб.")
    print(f"Вес сырых продуктов: {receipt.calc_weight(raw=True):.0f} г")
    print(f"Вес готового блюда: {receipt.calc_weight(raw=False):.0f} г")
    print(f"Время приготовления: {receipt.calc_cooking_time()} мин")