from abc import ABC
from abc import abstractmethod


class PresenterInterface(ABC):

    @abstractmethod
    def raise_exception_for_form_does_not_exists(self):
        pass

    @abstractmethod
    def raise_exception_for_form_closed(self):
        pass

    @abstractmethod
    def raise_exception_for_question_does_not_exists(self):
        pass

    @abstractmethod
    def raise_exception_for_question_does_not_belong_to_form(self):
        pass

    @abstractmethod
    def submit_form_response_return(self, response_id: int):
        pass

    @abstractmethod
    def raise_exception_for_invalid_user_response(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_question_type(self):
        pass

    @abstractmethod
    def raise_exception_for_multiple_responses_captured(self):
        pass
