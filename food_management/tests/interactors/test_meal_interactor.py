import pytest
from datetime import datetime
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from food_management.interactors.meal_interactor import MealInteractor
from food_management.exceptions.exceptions import InvalidMealId, \
    InvalidItemId, InvalidPreferenceItemId, DuplicateItemIds, \
    MealTimeOut
from food_management.interactors.storages.storage_interface import \
    StorageInterface
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface


def test_meal_interactor_with_invalid_meal_id_raises_exception(meal_dto):
    # Arrange
    user_id = 1
    invalid_meal_id = meal_dto.meal_id
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = MealInteractor(storage=storage)
    err = InvalidMealId(invalid_meal_id)
    storage.validate_meal_id.side_effect = err
    presenter.raise_exception_for_invalid_meal_id.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.food_mangement_wrapper(
            user_id=user_id,
            presenter=presenter,
            meal_dto=meal_dto
        )

    # Assert
    storage.validate_meal_id.assert_called_once_with(meal_id=invalid_meal_id)
    presenter.raise_exception_for_invalid_meal_id.\
        assert_called_once_with(err)

def test_meal_interactor_with_invalid_meal_item_ids_raises_exception(
    meal_dto):
    # Arrange
    user_id = 1
    meal_id = meal_dto.meal_id
    invalid_item_ids = [1]
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = MealInteractor(storage=storage)
    err = InvalidItemId(invalid_item_ids)
    storage.validate_item_ids.side_effect = err
    presenter.raise_exception_for_invalid_item_ids.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.food_mangement_wrapper(
            user_id=user_id,
            presenter=presenter,
            meal_dto=meal_dto
        )

    # Assert
    storage.validate_meal_id.assert_called_once_with(meal_id=meal_id)
    storage.validate_item_ids.assert_called_once_with(
        item_ids=invalid_item_ids)
    presenter.raise_exception_for_invalid_item_ids.\
        assert_called_once_with(err)

def test_meal_interactor_with_invalid_meal_preference_item_ids_raises_exception(
    meal_dto):
    # Arrange
    user_id = 1
    meal_id = meal_dto.meal_id
    item_ids = [1]
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = MealInteractor(storage=storage)
    err = InvalidPreferenceItemId(item_ids)
    storage.validate_preference_type_item_ids.side_effect = err
    presenter.raise_exception_for_invalid_preference_item_ids.side_effect = \
        NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.food_mangement_wrapper(
            user_id=user_id,
            presenter=presenter,
            meal_dto=meal_dto
        )

    # Assert
    storage.validate_meal_id.assert_called_once_with(meal_id=meal_id)
    storage.validate_item_ids.assert_called_once_with(
        item_ids=item_ids)
    storage.validate_preference_type_item_ids.assert_called_once_with(
        item_ids=item_ids)
    presenter.raise_exception_for_invalid_preference_item_ids.\
        assert_called_once_with(err)

def test_meal_interactor_with_duplicate_meal_item_ids_raises_exception(
    duplicate_meal_dto):
    # Arrange
    user_id = 1
    meal_id = duplicate_meal_dto.meal_id
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = MealInteractor(storage=storage)
    presenter.raise_exception_for_duplicate_item_ids.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.food_mangement_wrapper(
            user_id=user_id,
            presenter=presenter,
            meal_dto=duplicate_meal_dto
        )

    # Assert
    storage.validate_meal_id.assert_called_once_with(meal_id=meal_id)
    err = presenter.raise_exception_for_duplicate_item_ids.\
        call_args.kwargs['err']
    presenter.raise_exception_for_duplicate_item_ids.\
        assert_called_once_with(err=err)

def test_meal_interactor_with_invalid_meal_item_quantity_raises_exception(
    invalid_meal_dto):

    # Arrange
    user_id = 1
    meal_id = invalid_meal_dto.meal_id
    item_ids = [1]
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = MealInteractor(storage=storage)
    presenter.raise_exception_for_invalid_item_quantity.side_effect = \
        BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.food_mangement_wrapper(
            user_id=user_id,
            presenter=presenter,
            meal_dto=invalid_meal_dto
        )

    # Assert
    storage.validate_meal_id.assert_called_once_with(meal_id=meal_id)
    storage.validate_item_ids.assert_called_once_with(
        item_ids=item_ids)
    storage.validate_preference_type_item_ids.assert_called_once_with(
        item_ids= item_ids)
    err = presenter.raise_exception_for_invalid_item_quantity.\
        call_args.kwargs['err']
    presenter.raise_exception_for_invalid_item_quantity.\
        assert_called_once_with(err=err)

def test_meal_interactor_with_invalid_meal_time_raises_exception(meal_dto):

    # Arrange
    user_id = 1
    meal_id = meal_dto.meal_id
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = MealInteractor(storage=storage)
    err = MealTimeOut(
        datetime(2020, 11, 15)
    )
    storage.validate_meal_time.side_effect = err
    presenter.raise_exception_for_invalid_time_for_meal.side_effect = \
        BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.food_mangement_wrapper(
            user_id=user_id,
            presenter=presenter,
            meal_dto=meal_dto
        )

    # Assert
    storage.validate_meal_id.assert_called_once_with(meal_id=meal_id)
    storage.validate_meal_time.assert_called_once_with(meal_id=meal_id)
    presenter.raise_exception_for_invalid_time_for_meal.\
        assert_called_once_with(err=err)

def test_meal_interactor_with_valid_meal_details(meal_dto):

    # Arrange
    user_id = 1
    meal_id = meal_dto.meal_id
    item_ids = [1]
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = MealInteractor(storage=storage)

    # Act
    interactor.food_mangement_wrapper(
        user_id=user_id,
        presenter=presenter,
        meal_dto=meal_dto
    )

    # Assert
    storage.validate_meal_id.assert_called_once_with(meal_id=meal_id)
    storage.validate_meal_time.assert_called_once_with(meal_id=meal_id)
    storage.validate_item_ids.assert_called_once_with(
        item_ids=item_ids)
    storage.validate_preference_type_item_ids.assert_called_once_with(
        item_ids= item_ids)
    storage.create_or_update_meal_for_user.assert_called_once_with(
        user_id=user_id,
        meal_dto=meal_dto
    )