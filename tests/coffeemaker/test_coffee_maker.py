import pytest
from src.coffeemaker.coffee_maker import CoffeeMaker
from src.coffeemaker.exceptions.inventory_exception import InventoryException
from src.coffeemaker.recipe import Recipe


@pytest.fixture
def coffee_maker():
    return CoffeeMaker()


@pytest.fixture
def recipe_with_name():
    recipe = Recipe()
    recipe.set_name("Coffee")
    return recipe


@pytest.fixture
def new_recipe():
    recipe = Recipe()
    recipe.set_name("NewRecipe")
    return recipe


@pytest.fixture
def sample_recipes():
    recipes = []
    for name in ["Coffee 1", "Coffee 2", "Coffee 3"]:
        recipe = Recipe()
        recipe.set_name(name)
        recipes.append(recipe)
    return recipes


class TestCoffeeMaker:
    def test_get_recipes_returns_none_list(self, coffee_maker: CoffeeMaker):
        recipes = coffee_maker.get_recipes()
        expected_recipes = [None, None, None]
        assert recipes == expected_recipes

    def test_get_recipes_after_adding_recipes(
        self, coffee_maker: CoffeeMaker, sample_recipes: list[Recipe]
    ):
        for recipe in sample_recipes:
            coffee_maker.add_recipe(recipe)

        recipes = coffee_maker.get_recipes()
        assert recipes == sample_recipes

    def test_add_existing_recipe_returns_false(self, coffee_maker: CoffeeMaker):
        coffee_maker.add_recipe(recipe_with_name)
        result = coffee_maker.add_recipe(recipe_with_name)
        assert result is False

    def test_add_recipe_to_full_recipe_book_returns_false(
        self,
        coffee_maker: CoffeeMaker,
        recipe_with_name: Recipe,
        sample_recipes: list[Recipe],
    ):
        for recipe in sample_recipes:
            coffee_maker.add_recipe(recipe)
        result = coffee_maker.add_recipe(recipe_with_name)
        assert result is False

    def test_add_recipe_returns_true(
        self, coffee_maker: CoffeeMaker, recipe_with_name: Recipe
    ):
        result = coffee_maker.add_recipe(recipe_with_name)
        assert result is True

    def test_delete_recipe_with_negative_value_returns_none(
        self, coffee_maker: CoffeeMaker, recipe_with_name: Recipe
    ):
        coffee_maker.add_recipe(recipe_with_name)
        result = coffee_maker.delete_recipe(-1)
        assert result is None

    def test_delete_recipe_with_value_above_limit_returns_none(
        self, coffee_maker: CoffeeMaker, sample_recipes
    ):
        for recipe in sample_recipes:
            coffee_maker.add_recipe(recipe)
        result = coffee_maker.delete_recipe(3)
        assert result is None

    def test_delete_recipe_with_value_at_limit_but_no_recipe_returns_none(
        self, coffee_maker: CoffeeMaker, recipe_with_name: Recipe
    ):
        coffee_maker.add_recipe(recipe_with_name)
        result = coffee_maker.delete_recipe(2)
        assert result is None

    def test_delete_recipe_in_an_empty_list_returns_none(
        self, coffee_maker: CoffeeMaker
    ):
        result = coffee_maker.delete_recipe(0)
        assert result is None

    def test_delete_recipe_with_value_at_lower_limit_returns_deleted_recipe_name(
        self, coffee_maker: CoffeeMaker, recipe_with_name: Recipe
    ):
        coffee_maker.add_recipe(recipe_with_name)

        result = coffee_maker.delete_recipe(0)
        assert result == "Coffee"

    def test_delete_recipe_with_value_at_upper_limit_returns_deleted_recipe_name(
        self,
        coffee_maker: CoffeeMaker,
        sample_recipes: list[Recipe],
    ):
        for recipe in sample_recipes:
            coffee_maker.add_recipe(recipe)

        result = coffee_maker.delete_recipe(2)
        assert result == "Coffee 3"

    def test_edit_recipe_with_negative_value_returns_none(
        self, coffee_maker: CoffeeMaker, new_recipe: Recipe, recipe_with_name: Recipe
    ):
        coffee_maker.add_recipe(recipe_with_name)
        result = coffee_maker.edit_recipe(-1, new_recipe)
        assert result is None

    def test_edit_recipe_with_value_above_limit_returns_none(
        self, coffee_maker: CoffeeMaker, sample_recipes, new_recipe: Recipe
    ):
        for recipe in sample_recipes:
            coffee_maker.add_recipe(recipe)
        result = coffee_maker.edit_recipe(3, new_recipe)
        assert result is None

    def test_edit_recipe_with_value_at_limit_but_no_recipe_returns_none(
        self, coffee_maker: CoffeeMaker, recipe_with_name: Recipe, new_recipe: Recipe
    ):
        coffee_maker.add_recipe(recipe_with_name)
        result = coffee_maker.edit_recipe(2, new_recipe)
        assert result is None

    def test_edit_recipe_in_an_empty_list_returns_none(
        self, coffee_maker: CoffeeMaker, new_recipe: Recipe
    ):
        result = coffee_maker.edit_recipe(0, new_recipe)
        assert result is None

    def test_edit_recipe_with_value_at_lower_limit_returns_edited_recipe_name(
        self, coffee_maker: CoffeeMaker, recipe_with_name: Recipe, new_recipe: Recipe
    ):
        coffee_maker.add_recipe(recipe_with_name)

        result = coffee_maker.edit_recipe(0, new_recipe)
        assert result == "Coffee"

    def test_edit_recipe_with_value_at_upper_limit_returns_edited_recipe_name(
        self,
        coffee_maker: CoffeeMaker,
        sample_recipes: list[Recipe],
        new_recipe: Recipe,
    ):
        for recipe in sample_recipes:
            coffee_maker.add_recipe(recipe)

        result = coffee_maker.edit_recipe(2, new_recipe)
        assert result == "Coffee 3"

    def test_check_inventory_returns_inventory_string(self, coffee_maker: CoffeeMaker):
        coffee_maker.add_inventory(0, 1, 2, 3)
        inventory_str = coffee_maker.check_inventory()
        assert inventory_str == "Coffee: 15\nMilk: 16\nSugar: 17\nChocolate: 18"

    def test_add_inventory_with_non_positive_coffee_units_returns_none(
        self, coffee_maker: CoffeeMaker
    ):
        result = coffee_maker.add_inventory("0", "2", "2", "2")
        assert result is None

    def test_add_inventory_with_non_positive_milk_units_returns_none(
        self, coffee_maker: CoffeeMaker
    ):
        result = coffee_maker.add_inventory("2", "0", "2", "2")
        assert result is None

    def test_add_inventory_with_non_positive_sugar_units_returns_none(
        self, coffee_maker: CoffeeMaker
    ):
        result = coffee_maker.add_inventory("2", "2", "0", "2")
        assert result is None

    def test_add_inventory_with_non_positive_chocolate_units_returns_none(
        self, coffee_maker: CoffeeMaker
    ):
        result = coffee_maker.add_inventory("2", "2", "2", "0")
        assert result is None

    def test_add_inventory_with_positive_units_returns_none(
        self, coffee_maker: CoffeeMaker
    ):
        result = coffee_maker.add_inventory("2", "2", "2", "2")
        assert result is None

    def test_make_coffee_with_negative_recipe_index_returns_amt_paid(
        self, coffee_maker: CoffeeMaker
    ):
        amt_paid = 2
        result = coffee_maker.make_coffee(-1, amt_paid)
        assert result == amt_paid

    def test_make_coffee_with_recipe_index_above_limit_returns_amt_paid(
        self, coffee_maker: CoffeeMaker
    ):
        amt_paid = 2
        result = coffee_maker.make_coffee(3, amt_paid)
        assert result == amt_paid

    def test_make_coffee_with_recipe_index_within_limit_and_not_enough_money_returns_amt_paid(
        self, coffee_maker: CoffeeMaker
    ):
        amt_paid = 1
        result = coffee_maker.make_coffee(2, amt_paid)
        assert result == amt_paid

    def test_make_coffee_with_recipe_index_within_limit_and_enough_money_returns_change(
        self, coffee_maker: CoffeeMaker
    ):
        recipe1 = Recipe()
        recipe1.set_price(1)
        coffee_maker.add_recipe(recipe1)

        amt_paid = 2
        result = coffee_maker.make_coffee(0, amt_paid)
        assert result == amt_paid - recipe1.get_price()
