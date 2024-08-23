#!/usr/bin/env python3

# Ground truth:
# Obtain a dictionary of available items in the pantry.

# parameters:
#   minimum_quantity -- the minimum quantity that an item needs to have in order to be included in the returned dictionary

# returns:
#   available_items: dict -- a dictionary mapping pantry item names to their quantity (only including pantry items which have a quantity of minimum_quantity or higher)
#   None -- in case the self.get_all() method throws an exception

# To run the tests:
# python -m pytest -m unit

import pytest

from unittest.mock import MagicMock, patch

from src.controllers.recipecontroller import RecipeController

# Test cases:
# 1. Test if get_available_items() returns None if the self.get_all() method throws an exception
# 2. Test if get_available_items() returns a dictionary of available items in the pantry with a minimum quantity
# 3. Test if get_available_items() returns a dictionary of available items in the pantry with no minimum quantity

items = [
    {'name': 'Apple', 'quantity': 2},
    {'name': 'Banana', 'quantity': 5},
    {'name': 'Carrot', 'quantity': 2},
]

@pytest.mark.unit
def test_get_available_items_throws_exception():
    dao = MagicMock()  # Mock the DAO
    recipe_controller = RecipeController(items_dao=dao)

    recipe_controller.get_all = MagicMock(return_value=Exception)

    with pytest.raises(Exception):
        recipe_controller.get_available_items(minimum_quantity=1)

@pytest.mark.unit
def test_get_available_items_returns_dictionary_with_minimum_quantity():
    dao = MagicMock()  # Mock the DAO
    recipe_controller = RecipeController(items_dao=dao)

    recipe_controller.get_all = MagicMock(return_value=items)
    result = recipe_controller.get_available_items(minimum_quantity=2)

    assert result in [{'Banana': 5}]

@pytest.mark.unit
def test_get_available_items_returns_dictionary_with_no_minimum_quantity():
    dao = MagicMock()  # Mock the DAO
    recipe_controller = RecipeController(items_dao=dao)

    recipe_controller.get_all = MagicMock(return_value=items)
    result = recipe_controller.get_available_items()

    assert result in [{'Apple': 2, 'Banana': 5, 'Carrot': 2}]