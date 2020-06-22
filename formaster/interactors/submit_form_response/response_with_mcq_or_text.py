from abc import abstractmethod
from typing import Optional

from formaster.interactors.storages.storage_interface import StorageInterface
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.exceptions.exceptions import FormClosed, FormDoesNotExist, \
    QuestionDoesNotExist, QuestionDoesNotBelongToForm, InvalidUserResponse, \
    InvalidQuestionType, MultipleResponsesCaptured

class TextOrMCQSubmitFormResponseInteractor():

    def __init__(self, storage: StorageInterface, question_id: int,
                 form_id: int, user_id: int, mcq_choice_id: Optional[int],
                 text_response: Optional[str]):

        self.storage = storage
        self.question_id = question_id
        self.form_id = form_id
        self.user_id = user_id
        self.mcq_choice_id = mcq_choice_id
        self.text_response = text_response

    def submit_form_response_with_mcq_or_text_wrapper(
        self, presenter: PresenterInterface):

        try:
            response_id = self.submit_form_response_with_mcq_or_text()
        except MultipleResponsesCaptured:
            presenter.raise_exception_for_multiple_responses_captured()
        except FormDoesNotExist:
            presenter.raise_exception_for_form_does_not_exists()
        except FormClosed:
            presenter.raise_exception_for_form_closed()
        except QuestionDoesNotExist:
            presenter.raise_exception_for_question_does_not_exists()
        except QuestionDoesNotBelongToForm:
            presenter.raise_exception_for_question_does_not_belong_to_form()
        except InvalidUserResponse:
            presenter.raise_exception_for_invalid_user_response()
        except InvalidQuestionType:
            presenter.raise_exception_for_invalid_question_type()
        else:
            return presenter.submit_form_response_return(
                response_id=response_id)

    def submit_form_response_with_mcq_or_text(self):

        if self.mcq_choice_id and self.text_response:
            raise MultipleResponsesCaptured

        if self.mcq_choice_id:
            response_id = self._create_mcq_question_response()

        return response_id

    def _create_mcq_question_response(self):
        from formaster.interactors.submit_form_response.mcq_question import \
            MCQSubmitResponseInteractor

        interactor = MCQSubmitResponseInteractor(
            storage=self.storage,
            question_id=self.question_id,
            form_id=self.form_id,
            user_id=self.user_id,
            user_submitted_response=self.mcq_choice_id
        )

        response_id = interactor.submit_form_response()

        return response_id
