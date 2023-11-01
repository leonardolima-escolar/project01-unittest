from src.coffeemaker.recipe import Recipe


class RecipeBook:
    def __init__(self) -> None:
        self.__num_recipes = 3
        self.__recipe_array: list[Recipe] = [None] * self.__num_recipes

    def get_recipes(self) -> list[Recipe]:
        return self.__recipe_array

    def add_recipe(self, recipe: Recipe) -> bool:
        exists = False
        for i in range(len(self.__recipe_array)):
            if self.__recipe_array[i] is not None and recipe == self.__recipe_array[i]:
                exists = True
                break

        added = False
        if not exists:
            for i in range(len(self.__recipe_array)):
                if self.__recipe_array[i] is None:
                    self.__recipe_array[i] = recipe
                    added = True
                    break

        return added

    def delete_recipe(self, recipe_to_delete: int) -> str:
        if recipe_to_delete < 0 or recipe_to_delete >= len(self.__recipe_array):
            return None

        if self.__recipe_array[recipe_to_delete] is not None:
            recipe_name = self.__recipe_array[recipe_to_delete].get_name()
            self.__recipe_array[recipe_to_delete] = None
            return recipe_name

        return None

    def edit_recipe(self, recipe_to_edit: int, new_recipe: Recipe) -> str:
        if recipe_to_edit < 0 or recipe_to_edit >= len(self.__recipe_array):
            return None

        if self.__recipe_array[recipe_to_edit] is not None:
            recipe_name = self.__recipe_array[recipe_to_edit].get_name()
            self.__recipe_array[recipe_to_edit] = new_recipe
            # -> ?
            new_recipe.set_name(recipe_name)
            return recipe_name
