from abc import abstractmethod

from formaster.interactors.mixins.form_validation import FormValidationMixin
from formaster.interactors.storages.storage_interface import StorageInterface
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.exceptions.exceptions import FormClosed, FormDoesNotExist, \
    QuestionDoesNotExist, QuestionDoesNotBelongToForm, InvalidUserResponse, \
    InvalidQuestionType

class BaseSubmitFormResponseInteractor(FormValidationMixin):

    def __init__(self, storage: StorageInterface, question_id: int,
                 form_id: int, user_id: int):
        self.storage = storage
        self.question_id = question_id
        self.form_id = form_id
        self.user_id = user_id

    def submit_form_response_wrapper(self, user_id: int,
                                     question_id: int, form_id: int,
                                     presenter: PresenterInterface):
        try:
            response_id = self.submit_form_response()
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

    def submit_form_response(self):

        # TODO: validate form id
        self.storage.validate_form_id(form_id=self.form_id)

        # TODO: validate live form
        self.validate_for_live_form(form_id=self.form_id)

        # TODO: validate question id
        self.storage.validate_question_id(question_id=self.question_id)

        # TODO: validate question belong to the given form
        self.storage.validate_question_id_with_form(
            question_id=self.question_id, form_id=self.form_id
        )

        self._validate_user_response()
        self._validate_question_type()
        response_id = self._create_user_response()

        return response_id

    @abstractmethod
    def _validate_user_response(self):
        pass

    @abstractmethod
    def _validate_question_type(self):
        pass

    @abstractmethod
    def _create_user_response(self):
        pass
