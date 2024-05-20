#!/usr/bin/env python3

# Ground truth:
# Return a suitable recipe, if the recipe doesn't have a readiness greater than 0.1.
# Otherwise return None if the recipe could not be found.

import pytest

from unittest.mock import MagicMock
import unittest.mock as mock

from src.controllers.recipecontroller import RecipeController
from src.static.diets import Diet
from src.util.dao import getDao

# Test if get_recipe() returns None if the readiness list is empty
@pytest.mark.unit
def test_get_recipe_readiness_empty():
    controller = RecipeController(items_dao=getDao(collection_name='item'))

    controller.get_readiness_of_recipes = MagicMock(return_value=dict())
    result = controller.get_recipe(diet=Diet.NORMAL, take_best=True)

    assert result is None

# Test if get_recipe() returns a suitable recipe
@pytest.mark.unit
def test_get_recipe_diet_normal_take_best_true():
    dao = getDao(collection_name='item')
    controller = RecipeController(items_dao=dao)

    controller.get_readiness_of_recipes = MagicMock(return_value={'Recipe1': 0.5})
    result = controller.get_recipe(diet=Diet.NORMAL, take_best=True)

    assert result == 'Recipe1'

# Test if get_recipe() returns a non suitable recipe
@pytest.mark.unit
def test_get_recipe_diet_vegetarian_take_best_false():
    dao = getDao(collection_name='item')
    controller = RecipeController(items_dao=dao)

    controller.get_readiness_of_recipes = MagicMock(return_value={'Recipe1': 0.5, 'Recipe2': 0.8})
    result = controller.get_recipe(diet=Diet.VEGETARIAN, take_best=False)

    assert result in ['Recipe1', 'Recipe2']

# Test if get_recipe() returns a suitable recipe
@pytest.mark.unit
def test_get_recipe_diet_vegan_take_best_true():
    dao = getDao(collection_name='item')
    controller = RecipeController(items_dao=dao)

    with mock.patch("random.randint", return_value=1) as mock_random:
        controller.get_readiness_of_recipes = MagicMock(return_value={'Recipe1': 0.5, 'Recipe2': 0.8})
        result = controller.get_recipe(diet=Diet.VEGAN, take_best=True)
        assert result == 'Recipe2'
