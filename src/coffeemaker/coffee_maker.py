from typing import Optional

from src.coffeemaker.exceptions.inventory_exception import InventoryException
from src.coffeemaker.recipe import Recipe
from src.coffeemaker.recipe_book import RecipeBook
from src.coffeemaker.inventory import Inventory


class CoffeeMaker:
    def __init__(self) -> None:
        self.__recipe_book = RecipeBook()
        self.__inventory = Inventory()

    def add_recipe(self, r: Recipe) -> bool:
        return self.__recipe_book.add_recipe(r)

    def delete_recipe(self, recipe_to_delete: int) -> Optional[str]:
        return self.__recipe_book.delete_recipe(recipe_to_delete)

    def edit_recipe(self, recipe_to_edit: int, r: Recipe) -> Optional[str]:
        return self.__recipe_book.edit_recipe(recipe_to_edit, r)

    def add_inventory(
        self, amt_coffee: str, amt_milk: str, amt_sugar: str, amt_chocolate: str
    ) -> None:
        try:
            self.__inventory.add_coffee(amt_coffee)
            self.__inventory.add_milk(amt_milk)
            self.__inventory.add_sugar(amt_sugar)
            self.__inventory.add_chocolate(amt_chocolate)
        except InventoryException as e:
            raise InventoryException(str(e))

    def check_inventory(self) -> str:
        return str(self.__inventory)

    def make_coffee(self, recipe_to_purchase: int, amt_paid: int) -> int:
        change = 0

        if (
            recipe_to_purchase < 0
            or recipe_to_purchase >= len(self.__recipe_book.get_recipes())
            or self.__recipe_book.get_recipes()[recipe_to_purchase] is None
        ):
            change = amt_paid
        else:
            if (
                self.__recipe_book.get_recipes()[recipe_to_purchase].get_price()
                <= amt_paid
            ):
                if self.__inventory.use_ingredients(
                    self.__recipe_book.get_recipes()[recipe_to_purchase]
                ):
                    change = (
                        amt_paid
                        - self.__recipe_book.get_recipes()[
                            recipe_to_purchase
                        ].get_price()
                    )
                else:
                    change = amt_paid
            else:
                change = amt_paid

        return change

    def get_recipes(self) -> list[Recipe]:
        return self.__recipe_book.get_recipes()
