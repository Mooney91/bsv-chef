import pytest
from unittest.mock import MagicMock
from unittest.mock import patch

from src.controllers.recipecontroller import RecipeController
from src.static.diets import Diet

class TestGetRecipeReadiness:

    @pytest.fixture
    def sut_recipecontroller(self):
        """
        Fixture for creating a RecipeController object with a mocked DAO.
        Returns: RecipeController: An instance of RecipeController with a mocked DAO.
        """

        mocked_dao = MagicMock()

        recipes = [
            {
                "name": "Banana Bread",
                "diets": [
                    "normal", "vegetarian"
                ],
                "ingredients": {
                    "Butter": 100,
                    "Banana": 4,
                    "Sugar": 200,
                    "Egg": 1,
                    "Vanilla Sugar": 1,
                    "Baking Powder": 0.5,
                    "Salt": 5,
                    "Cinnamon": 10,
                    "Flour": 220,
                    "Walnuts": 10
                }
            },
            {
                "name": "Pancakes",
                "diets": [
                    "normal", "vegetarian"
                ],
                "ingredients": {
                    "Egg": 3,
                    "Milk": 100,
                    "Yoghurt": 200,
                    "Flour": 150,
                    "Baking Powder": 1,
                    "Salt": 5,
                    "Sugar": 25
                }
            },
            {
                "name": "Whole Grain Bread",
                "diets": [
                    "normal", "vegetarian", "vegan"
                ],
                "ingredients": {
                    "Flour": 500,
                    "Walnuts": 20,
                    "Yeast": 1,
                    "Salt": 10,
                    "Vinegar": 30
                }
            }
        ]

        rc = RecipeController(items_dao=mocked_dao)

        return rc

    # ATTEMPT TO MOCK DIET?
    # @pytest.fixture
    # @patch('src.controllers.recipecontroller.Diet', autospec=True)
    # def mocked_diet_normal(mockedDiet):
    #     mockedDiet.name.return_value = "NORMAL"
    #     return mockedDiet

    @pytest.mark.unit
    def test_get_recipe_1(self, sut_recipecontroller):
        """
        Test case 1: 
        """
        result = sut_recipecontroller.get_recipe(Diet(1), True)
        recipe = "recipe"

        assert result == recipe

    @pytest.mark.unit
    def test_get_recipe_2(self, sut_recipecontroller):
        """
        Test case 2: 
        """
        result = sut_recipecontroller.get_recipe(Diet(2), True)
        recipe = "recipe"

        assert result == recipe

    @pytest.mark.unit
    def test_get_recipe_3(self, sut_recipecontroller):
        """
        Test case 3: 
        """
        result = sut_recipecontroller.get_recipe(Diet(3), True)
        recipe = "recipe"

        assert result == recipe

    @pytest.mark.unit
    def test_get_recipe_4(self, sut_recipecontroller):
        """
        Test case 4: 
        """
        result = sut_recipecontroller.get_recipe(Diet(1), False)
        recipe = "recipe"

        assert result == recipe

    @pytest.mark.unit
    def test_get_recipe_5(self, sut_recipecontroller):
        """
        Test case 5: 
        """
        result = sut_recipecontroller.get_recipe(Diet(1), True)
        recipe = "recipe"

        assert result == None