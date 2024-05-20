#!/usr/bin/env python3

# Command: python -m pytest -m unit

# Test get_recipe() method

# Ground truth:
# Return a suitable recipe, if the recipe doesn't have a readiness greater than 0.1.
# Otherwise return None if the recipe could not be found.

# Actions and expected results:
# a. Readiness list can be empty [None]
# b. 

# Conditions:
# a. Diet can be [NORMAL; VEGETARIAN; VEGAN]
# b. Take best can be [True; False]

# Combinations:
# Expected results:
#
# | Readiness list  | Diet       | Take best | Result |
# |-----------------|------------|-----------|--------|
# | Empty           | Normal     | True      | None   |
# | -               | Vegetarian | False     | None   |
# | -               | Vegan      |
# |
# |

import pytest

from unittest.mock import MagicMock

from src.controllers.recipecontroller import RecipeController
from src.static.diets import Diet
from src.util.dao import getDao

@pytest.mark.unit
def test_get_recipe_readiness_empty():
    controller = RecipeController(items_dao=getDao(collection_name="item"))

    controller.get_readiness_of_recipes = MagicMock(return_value=dict())

    print("Test: " + controller.get_readiness_of_recipes(recipes=[], diet=Diet.NORMAL))

    result = controller.get_recipe(diet=Diet.NORMAL, take_best=True)

    assert result is None
