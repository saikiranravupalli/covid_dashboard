from abc import ABC, abstractmethod
from typing import List
from food_management.interactors.storages.dtos import MealDto

class StorageInterface(ABC):

    @abstractmethod
    def validate_meal_id(self, meal_id: int):
        pass

    @abstractmethod
    def validate_item_ids(self, item_ids: List[int]):
        pass

    @abstractmethod
    def validate_preference_type_item_ids(self, item_ids: List[int]):
        pass

    @abstractmethod
    def validate_meal_time(self, meal_id: int):
        pass

    @abstractmethod
    def create_or_update_meal_for_user(self, user_id: int, meal_dto: MealDto):
        pass
