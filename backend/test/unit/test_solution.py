#!/usr/bin/env python3

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

from src.controllers.recipecontroller import RecipeController
from src.static.diets import Diet

from src.util.dao import getDao
from unittest.mock import MagicMock

@pytest.mark.unit
def test_get_recipe_readiness_empty():
    dao = getDao(collection_name='item')
    controller = RecipeController(items_dao=dao)

    controller.get_readiness_of_recipes = MagicMock(return_value=[])
    result = controller.get_recipe(diet=Diet.NORMAL, take_best=True)

    print("Hello, World!")

    assert result is None
