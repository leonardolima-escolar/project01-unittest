from src.coffeemaker.exceptions.inventory_exception import InventoryException
from src.coffeemaker.recipe import Recipe


class Inventory:
    def __init__(self) -> None:
        self.__coffee: int = 15
        self.__milk: int = 15
        self.__sugar: int = 15
        self.__chocolate: int = 15

    def get_chocolate(self) -> int:
        return self.__chocolate

    def set_chocolate(self, chocolate: int) -> None:
        if chocolate >= 0:
            self.__chocolate = chocolate
        else:
            raise InventoryException("Units of chocolate must be a positive integer")

    def add_chocolate(self, chocolate: str) -> None:
        try:
            amt_chocolate = int(chocolate)
            if amt_chocolate >= 0:
                self.__chocolate += amt_chocolate
            else:
                raise InventoryException(
                    "Units of chocolate must be a positive integer"
                )
        except ValueError:
            raise InventoryException("Units of chocolate must be a positive integer")

    def get_coffee(self) -> int:
        return self.__coffee

    def set_coffee(self, coffee: int) -> None:
        if coffee >= 0:
            self.__coffee = coffee
        else:
            raise InventoryException("Units of coffee must be a positive integer")

    def add_coffee(self, coffee: str) -> None:
        try:
            amt_coffee = int(coffee)
            if amt_coffee >= 0:
                self.__coffee += amt_coffee
            else:
                raise InventoryException("Units of coffee must be a positive integer")
        except ValueError:
            raise InventoryException("Units of coffee must be a positive integer")

    def get_milk(self) -> int:
        return self.__milk

    def set_milk(self, milk: int) -> None:
        if milk >= 0:
            self.__milk = milk
        else:
            raise InventoryException("Units of milk must be a positive integer")

    def add_milk(self, milk: str) -> None:
        try:
            amt_milk = int(milk)
            if amt_milk >= 0:
                self.__milk += amt_milk
            else:
                raise InventoryException("Units of milk must be a positive integer")
        except ValueError:
            raise InventoryException("Units of milk must be a positive integer")

    def get_sugar(self) -> int:
        return self.__sugar

    def set_sugar(self, sugar: int) -> None:
        if sugar >= 0:
            self.__sugar = sugar
        else:
            raise InventoryException("Units of sugar must be a positive integer")

    def add_sugar(self, sugar: str) -> None:
        try:
            amt_sugar = int(sugar)
            if amt_sugar >= 0:
                self.__sugar += amt_sugar
            else:
                raise InventoryException("Units of sugar must be a positive integer")
        except ValueError:
            raise InventoryException("Units of sugar must be a positive integer")

    def enough_ingredients(self, r: Recipe) -> bool:
        is_enough = True
        if self.__coffee < r.get_amt_coffee():
            is_enough = False
        if self.__milk < r.get_amt_milk():
            is_enough = False
        if self.__sugar < r.get_amt_sugar():
            is_enough = False
        if self.__chocolate < r.get_amt_chocolate():
            is_enough = False
        return is_enough

    def use_ingredients(self, r: Recipe) -> bool:
        if self.enough_ingredients(r):
            self.__coffee -= r.get_amt_coffee()
            self.__milk -= r.get_amt_milk()
            self.__sugar -= r.get_amt_sugar()
            self.__chocolate -= r.get_amt_chocolate()
            return True
        else:
            return False

    def __str__(self) -> str:
        result = "Coffee: {}\nMilk: {}\nSugar: {}\nChocolate: {}".format(
            self.__coffee, self.__milk, self.__sugar, self.__chocolate
        )
        return result
