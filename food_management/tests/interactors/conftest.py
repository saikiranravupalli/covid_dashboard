import pytest
from datetime import date
from typing import List
from food_management.interactors.storages.dtos import ItemQuantityDto, \
    MealDto

@pytest.fixture()
def item_quantity_dtos():
    item_quantity_dtos = [
        ItemQuantityDto(
            item_id=1,
            quantity=2
        )
    ]
    return item_quantity_dtos

@pytest.fixture()
def meal_dto(item_quantity_dtos):
    meal_dto = MealDto(
        meal_id=1,
        on_date=date(2020, 11, 15),
        preference_type='CUSTOM',
        items=item_quantity_dtos
    )
    return meal_dto

@pytest.fixture()
def duplicate_item_quantity_dtos():
    item_quantity_dtos = [
        ItemQuantityDto(
            item_id=1,
            quantity=2
        ),
        ItemQuantityDto(
            item_id=1,
            quantity=2
        )
    ]
    return item_quantity_dtos

@pytest.fixture()
def duplicate_meal_dto(duplicate_item_quantity_dtos):
    meal_dto = MealDto(
        meal_id=1,
        on_date=date(2020, 11, 15),
        preference_type='CUSTOM',
        items=duplicate_item_quantity_dtos
    )
    return meal_dto

@pytest.fixture()
def invalid_item_quantity_dtos():
    item_quantity_dtos = [
        ItemQuantityDto(
            item_id=1,
            quantity=-2
        )
    ]
    return item_quantity_dtos

@pytest.fixture()
def invalid_meal_dto(invalid_item_quantity_dtos):
    meal_dto = MealDto(
        meal_id=1,
        on_date=date(2020, 11, 15),
        preference_type='CUSTOM',
        items=invalid_item_quantity_dtos
    )
    return meal_dto
