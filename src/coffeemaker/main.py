from src.coffeemaker.coffee_maker import CoffeeMaker
from src.coffeemaker.recipe import Recipe
from src.coffeemaker.exceptions.recipe_exception import RecipeException


class Main:
    def __init__(self):
        self.__coffee_maker = CoffeeMaker()

    def main_menu(self):
        print("1. Add a recipe")
        print("2. Delete a recipe")
        print("3. Edit a recipe")
        print("4. Add inventory")
        print("5. Check inventory")
        print("6. Make coffee")
        print("0. Exit\n")

        try:
            user_input = int(
                self.__input_output(
                    "Please press the number that corresponds to what you would like the coffee maker to do."
                )
            )

            if 0 <= user_input <= 6:
                if user_input == 1:
                    self.add_recipe()
                elif user_input == 2:
                    self.delete_recipe()
                elif user_input == 3:
                    self.edit_recipe()
                elif user_input == 4:
                    self.add_inventory()
                elif user_input == 5:
                    self.check_inventory()
                elif user_input == 6:
                    self.make_coffee()
                elif user_input == 0:
                    exit(0)
            else:
                print("Please enter a number from 0 - 6")
                self.main_menu()
        except ValueError:
            print("Please enter a number from 0 - 6")
            self.main_menu()

    def add_recipe(self):
        name = self.__input_output("\nPlease enter the recipe name: ")
        price_string = self.__input_output("\nPlease enter the recipe price: $")
        coffee_string = self.__input_output(
            "\nPlease enter the units of coffee in the recipe: "
        )
        milk_string = self.__input_output(
            "\nPlease enter the units of milk in the recipe: "
        )
        sugar_string = self.__input_output(
            "\nPlease enter the units of sugar in the recipe: "
        )
        chocolate_string = self.__input_output(
            "\nPlease enter the units of chocolate in the recipe: "
        )

        r = Recipe()
        try:
            r.set_name(name)
            r.set_price(price_string)
            r.set_amt_coffee(coffee_string)
            r.set_amt_milk(milk_string)
            r.set_amt_sugar(sugar_string)
            r.set_amt_chocolate(chocolate_string)

            recipe_added = self.__coffee_maker.add_recipe(r)

            if recipe_added:
                print(name + " successfully added.\n")
            else:
                print(name + " could not be added.\n")
        except RecipeException as e:
            print(e)
        finally:
            self.main_menu()

    def delete_recipe(self):
        recipes = self.__coffee_maker.get_recipes()
        for i in range(len(recipes)):
            if recipes[i] is not None:
                print(f"{i + 1}. {recipes[i].get_name()}")

        recipe_to_delete = self.__recipe_list_selection(
            "Please select the number of the recipe to delete."
        )

        if recipe_to_delete < 0:
            print("Invalid selection")
            self.main_menu()

        recipe_deleted = self.__coffee_maker.delete_recipe(recipe_to_delete)

        if recipe_deleted is not None:
            print(f"{recipe_deleted} successfully deleted.\n")
        else:
            print("Selected recipe doesn't exist and could not be deleted.\n")
        self.main_menu()

    def edit_recipe(self):
        recipes = self.__coffee_maker.get_recipes()
        for i in range(len(recipes)):
            if recipes[i] is not None:
                print(f"{i + 1}. {recipes[i].get_name()}")

        recipe_to_edit = self.__recipe_list_selection(
            "Please select the number of the recipe to edit."
        )

        if recipe_to_edit < 0:
            print("Invalid selection")
            self.main_menu()

        price_string = self.__input_output("\nPlease enter the recipe price: $")
        coffee_string = self.__input_output(
            "\nPlease enter the units of coffee in the recipe: "
        )
        milk_string = self.__input_output(
            "\nPlease enter the units of milk in the recipe: "
        )
        sugar_string = self.__input_output(
            "\nPlease enter the units of sugar in the recipe: "
        )
        chocolate_string = self.__input_output(
            "\nPlease enter the units of chocolate in the recipe: "
        )

        new_recipe = Recipe()
        try:
            new_recipe.set_price(price_string)
            new_recipe.set_amt_coffee(coffee_string)
            new_recipe.set_amt_milk(milk_string)
            new_recipe.set_amt_sugar(sugar_string)
            new_recipe.set_amt_chocolate(chocolate_string)

            recipe_edited = self.__coffee_maker.edit_recipe(recipe_to_edit, new_recipe)

            if recipe_edited is not None:
                print(f"{recipe_edited} successfully edited.\n")
            else:
                print(f"{recipe_edited} could not be edited.\n")
        except RecipeException as e:
            print(e)
        finally:
            self.main_menu()

    def add_inventory(self):
        coffee_string = self.__input_output(
            "\nPlease enter the units of coffee to add: "
        )
        milk_string = self.__input_output("\nPlease enter the units of milk to add: ")
        sugar_string = self.__input_output("\nPlease enter the units of sugar to add: ")
        chocolate_string = self.__input_output(
            "\nPlease enter the units of chocolate to add: "
        )

        try:
            self.__coffee_maker.add_inventory(
                coffee_string, milk_string, sugar_string, chocolate_string
            )
            print("Inventory successfully added")
        except InventoryException as e:
            print("Inventory was not added")
        finally:
            self.main_menu()

    def check_inventory(self):
        print(self.__coffee_maker.check_inventory())
        self.main_menu()

    def make_coffee(self):
        recipes = self.__coffee_maker.get_recipes()
        for i in range(len(recipes)):
            if recipes[i] is not None:
                print(f"{i + 1}. {recipes[i].get_name()}")

        recipe_to_purchase = self.__recipe_list_selection(
            "Please select the number of the recipe to purchase."
        )

        amount_paid = self.__input_output("Please enter the amount you wish to pay: ")
        try:
            amt_paid = int(amount_paid)
        except ValueError:
            print("Please enter a positive integer")
            self.main_menu()

        change = self.__coffee_maker.make_coffee(recipe_to_purchase, amt_paid)

        if change == amt_paid:
            print("Insufficient funds to purchase.")
        else:
            print(
                f"Thank you for purchasing {self.__coffee_maker.get_recipes()[recipe_to_purchase].get_name()}"
            )
        print(f"Your change is: {change}\n")
        self.main_menu()

    def __input_output(self, message):
        try:
            user_input = input(message)
            return user_input
        except Exception as e:
            print("Error reading in value")
            self.main_menu()

    def __recipe_list_selection(self, message):
        user_selection = self.__input_output(message)
        recipe = 0
        try:
            recipe = int(user_selection) - 1
            if 0 <= recipe <= 2:
                return recipe
            else:
                return -1
        except ValueError:
            print("Please select a number from 1-3.")
            return -1

    def start(self):
        print("Welcome to the CoffeeMaker!\n")
        self.main_menu()
