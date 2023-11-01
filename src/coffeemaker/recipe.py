from src.coffeemaker.exceptions.recipe_exception import RecipeException


class Recipe:
    def __init__(self) -> None:
        self.__name: str = ""
        self.__price: int = 0
        self.__amt_coffee: int = 0
        self.__amt_milk: int = 0
        self.__amt_sugar: int = 0
        self.__amt_chocolate: int = 0

    def get_amt_chocolate(self) -> int:
        return self.__amt_chocolate

    def set_amt_chocolate(self, chocolate: str) -> None:
        try:
            amt_chocolate = int(chocolate)
            if amt_chocolate >= 0:
                self.__amt_chocolate = amt_chocolate
            else:
                raise RecipeException("Units of chocolate must be a positive integer")
        except ValueError:
            raise RecipeException("Units of chocolate must be a positive integer")

    def get_amt_coffee(self) -> int:
        return self.__amt_coffee

    def set_amt_coffee(self, coffee: str) -> None:
        try:
            amt_coffee = int(coffee)
            if amt_coffee >= 0:
                self.__amt_coffee = amt_coffee
            else:
                raise RecipeException("Units of coffee must be a positive integer")
        except ValueError:
            raise RecipeException("Units of coffee must be a positive integer")

    def get_amt_milk(self) -> int:
        return self.__amt_milk

    def set_amt_milk(self, milk: str) -> None:
        try:
            amt_milk = int(milk)
            if amt_milk >= 0:
                self.__amt_milk = amt_milk
            else:
                raise RecipeException("Units of milk must be a positive integer")
        except ValueError:
            raise RecipeException("Units of milk must be a positive integer")

    def get_amt_sugar(self) -> int:
        return self.__amt_sugar

    def set_amt_sugar(self, sugar: str) -> None:
        try:
            amt_sugar = int(sugar)
            if amt_sugar >= 0:
                self.__amt_sugar = amt_sugar
            else:
                raise RecipeException("Units of sugar must be a positive integer")
        except ValueError:
            raise RecipeException("Units of sugar must be a positive integer")

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        if name is not None:
            self.__name = name

    def get_price(self) -> int:
        return self.__price

    def set_price(self, price: str) -> None:
        try:
            amt_price = int(price)
            if amt_price >= 0:
                self.__price = amt_price
            else:
                raise RecipeException("Price must be a positive integer")
        except ValueError:
            raise RecipeException("Price must be a positive integer")

    def __str__(self) -> str:
        return self.__name

    def __hash__(self) -> int:
        return hash(self.__name)

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if not isinstance(other, Recipe):
            return False
        return self.__name == other.__name  # pylint: disable=protected-access
