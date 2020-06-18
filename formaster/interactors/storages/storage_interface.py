from abc import ABC, abstractmethod
from typing import List

class StorageInterface(ABC):

    @abstractmethod
    def validate_form_id(self, form_id: int):
        pass

    @abstractmethod
    def validate_for_live_form(self, form_id: int):
        pass

    @abstractmethod
    def validate_question_id(self, question_id: int):
        pass

    @abstractmethod
    def validate_question_id_with_form(self, question_id: int, form_id: int):
        pass

    @abstractmethod
    def get_option_ids_for_question(self, question_id: int) -> List[int]:
        pass

    @abstractmethod
    def create_user_response(self, user_id: int, question_id: int,
                             user_submitted_response: int) -> int:
        pass

    @abstractmethod
    def get_question_type(self, question_id: int) -> str:
        pass
