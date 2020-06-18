from formaster.interactors.storages.storage_interface import StorageInterface
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.interactors.submit_form_response.base import \
    BaseSubmitFormResponseInteractor
from formaster.exceptions.exceptions import InvalidUserResponse, \
    InvalidQuestionType

class MCQSubmitResponseInteractor(BaseSubmitFormResponseInteractor):

    def __init__(self, storage: StorageInterface,
                 question_id: int, form_id: int,
                 user_id: int, user_submitted_response: int):

        super().__init__(storage, question_id, form_id, user_id)
        self.user_id = user_id
        self.question_id = question_id
        self.user_submitted_response = user_submitted_response

    def _validate_user_response(self):
        option_ids = self.storage.get_option_ids_for_question(
            question_id=self.question_id)

        is_user_response_not_in_option_ids = \
            self.user_submitted_response not in option_ids

        if is_user_response_not_in_option_ids:
            raise InvalidUserResponse

    def _validate_question_type(self):
        question_type = self.storage.get_question_type(self.question_id)

        is_not_mcq_question_type = question_type != 'MCQ'

        if is_not_mcq_question_type:
            raise InvalidQuestionType

    def _create_user_response(self):
        response_id = self.storage.create_user_response(
            user_id=self.user_id,
            question_id=self.question_id,
            user_submitted_response=self.user_submitted_response
        )

        return response_id
