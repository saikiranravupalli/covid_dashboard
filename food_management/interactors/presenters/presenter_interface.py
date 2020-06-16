from abc import ABC, abstractmethod

class PresenterInterface(ABC):

    @abstractmethod
    def raise_exception_for_invalid_meal_id(self, err):
        pass

    @abstractmethod
    def raise_exception_for_invalid_item_ids(self, err):
        pass

    @abstractmethod
    def raise_exception_for_invalid_preference_item_ids(self, err):
        pass

    @abstractmethod
    def raise_exception_for_duplicate_item_ids(self, err):
        pass

    @abstractmethod
    def raise_exception_for_invalid_item_quantity(self, err):
        pass

    @abstractmethod
    def raise_exception_for_invalid_time_for_meal(self, err):
        pass
