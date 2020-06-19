import pytest
from unittest.mock import create_autospec, patch
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from formaster.interactors.storages.storage_interface import StorageInterface
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.exceptions.exceptions import MultipleResponsesCaptured
from formaster.interactors.submit_form_response.response_with_mcq_or_text import \
    TextOrMCQSubmitFormResponseInteractor
from formaster.interactors.submit_form_response.mcq_question import \
    MCQSubmitResponseInteractor

def test_submit_response_with_multiple_responses_raises_exception():

    # Arrange
    question_id = 1
    user_id = 1
    form_id = 1
    mcq_choice_id = 1
    text_response = 'Hi'
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = TextOrMCQSubmitFormResponseInteractor(
        storage=storage,
        question_id=question_id,
        form_id=form_id,
        user_id=user_id,
        mcq_choice_id=mcq_choice_id,
        text_response=text_response
    )

    presenter.raise_exception_for_multiple_responses_captured.side_effect = \
        BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.submit_form_response_with_mcq_or_text_wrapper(
            presenter=presenter)

    # Assert
    presenter.raise_exception_for_multiple_responses_captured.\
        assert_called_once()

def test_submit_response_with_mcq_choice_id_returns_response_id():

    # Arrange
    question_id = 1
    user_id = 1
    form_id = 1
    mcq_choice_id = 1
    text_response = None
    response_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = TextOrMCQSubmitFormResponseInteractor(
        storage=storage,
        question_id=question_id,
        form_id=form_id,
        user_id=user_id,
        mcq_choice_id=mcq_choice_id,
        text_response=text_response
    )

    # Act
    with patch.object(MCQSubmitResponseInteractor, 'submit_form_response',
        return_value=1):

        interactor.submit_form_response_with_mcq_or_text_wrapper(
            presenter=presenter)

    # Assert
    presenter.submit_form_response_return.assert_called_once_with(
        response_id=response_id)
