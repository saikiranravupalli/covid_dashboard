from collections import Counter
from food_management.interactors.storages.dtos import \
    MealDto
from food_management.interactors.storages.storage_interface import \
    StorageInterface
from food_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from food_management.exceptions.exceptions import InvalidMealId, \
    InvalidItemId, InvalidPreferenceItemId, DuplicateItemIds, \
    InvalidItemQuantity, MealTimeOut

class MealInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def food_mangement_wrapper(self, user_id: int,
                               meal_dto: MealDto,
                               presenter: PresenterInterface):
        try:
            self.food_management(
                user_id=user_id,
                meal_dto=meal_dto
            )
        except InvalidMealId as err:
            presenter.raise_exception_for_invalid_meal_id(err=err)
        except InvalidItemId as err:
            presenter.raise_exception_for_invalid_item_ids(err=err)
        except InvalidPreferenceItemId as err:
            presenter.raise_exception_for_invalid_preference_item_ids(err=err)
        except DuplicateItemIds as err:
            presenter.raise_exception_for_duplicate_item_ids(err=err)
        except InvalidItemQuantity as err:
            presenter.raise_exception_for_invalid_item_quantity(err=err)
        except MealTimeOut as err:
            presenter.raise_exception_for_invalid_time_for_meal(err=err)
            

    def food_management(self, user_id: int, meal_dto: MealDto):
        items = meal_dto.items
        item_ids = [item.item_id for item in items]

        # TODO: validate_meal_id
        self.storage.validate_meal_id(meal_id=meal_dto.meal_id)

        # TODO: validate_meal_time
        self.storage.validate_meal_time(meal_dto.meal_id)

        # TODO: check_duplication_of_item_ids
        self._check_duplicate_item_ids(item_ids=item_ids)

        # TODO: validate_item_ids
        self.storage.validate_item_ids(item_ids=item_ids)

        # TODO: validate_item_ids_related_to_preference_type
        self.storage.validate_preference_type_item_ids(item_ids=item_ids)

        # TODO: validate_items_quantity
        self._validate_items_quantity(items)

        # TODO: if yes create_meal else update
        self.storage.create_or_update_meal_for_user(
            user_id=user_id,
            meal_dto=meal_dto
        )

    @staticmethod
    def _check_duplicate_item_ids(item_ids):

        duplicate_items = [
            item_id 
            for item_id, item_id_count in Counter(item_ids).items()
            if item_id_count>1
        ]

        if duplicate_items:
            raise DuplicateItemIds(duplicate_items)

    @staticmethod
    def _validate_items_quantity(item_dtos):
        invalid_items_quantity = [
            item_dto
            for item_dto in item_dtos
            if item_dto.quantity < 0
        ]

        if invalid_items_quantity:
            raise InvalidItemQuantity(invalid_items_quantity)
 