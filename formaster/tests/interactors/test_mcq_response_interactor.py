import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from formaster.interactors.storages.storage_interface import StorageInterface
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.exceptions.exceptions import InvalidUserResponse
from formaster.interactors.submit_form_response.mcq_question import \
    MCQSubmitResponseInteractor

def test_validate_user_response_with_invalid_user_response_raises_exception():

    # Arrange
    question_id = 1
    user_id = 1
    form_id = 1
    user_submitted_response = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = MCQSubmitResponseInteractor(
        storage=storage,
        question_id=question_id,
        form_id=form_id,
        user_id=user_id,
        user_submitted_response=user_submitted_response
    )

    presenter.raise_exception_for_invalid_user_response.side_effect = \
        BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.submit_form_response_wrapper(
            user_id=user_id,
            form_id=form_id,
            question_id=question_id,
            presenter=presenter
        )

    # Assert
    storage.validate_form_id.assert_called_once_with(form_id=form_id)
    storage.validate_question_id.assert_called_once_with(
        question_id=question_id)
    storage.validate_question_id_with_form.assert_called_once_with(
        form_id=form_id, question_id=question_id)
    storage.get_option_ids_for_question.assert_called_once_with(
        question_id=question_id)
    presenter.raise_exception_for_invalid_user_response.assert_called_once()

def test_validate_user_response_with_invalid_question_type_raises_exception():

    # Arrange
    question_id = 1
    user_id = 1
    form_id = 1
    user_submitted_response = 1
    question_type = ''
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = MCQSubmitResponseInteractor(
        storage=storage,
        question_id=question_id,
        form_id=form_id,
        user_id=user_id,
        user_submitted_response=user_submitted_response
    )

    storage.get_option_ids_for_question.return_value = [1, 2]
    storage.get_question_type.return_value = question_type
    presenter.raise_exception_for_invalid_question_type.side_effect = \
        BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.submit_form_response_wrapper(
            user_id=user_id,
            form_id=form_id,
            question_id=question_id,
            presenter=presenter
        )

    # Assert
    storage.validate_form_id.assert_called_once_with(form_id=form_id)
    storage.validate_question_id.assert_called_once_with(
        question_id=question_id)
    storage.validate_question_id_with_form.assert_called_once_with(
        form_id=form_id, question_id=question_id)
    storage.get_option_ids_for_question.assert_called_once_with(
        question_id=question_id)
    storage.get_question_type.assert_called_once_with(question_id=question_id)
    presenter.raise_exception_for_invalid_question_type.assert_called_once()

def test_validate_user_response_with_valid_details_returns_user_response():

    # Arrange
    question_id = 1
    user_id = 1
    form_id = 1
    user_submitted_response = 1
    response_id = 1
    question_type = 'MCQ'
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = MCQSubmitResponseInteractor(
        storage=storage,
        question_id=question_id,
        form_id=form_id,
        user_id=user_id,
        user_submitted_response=user_submitted_response
    )

    storage.get_option_ids_for_question.return_value = [1, 2]
    storage.get_question_type.return_value = question_type
    storage.create_user_response.return_value = response_id
    presenter.submit_form_response_return.return_value = response_id

    # Act
    actual_response_id = interactor.submit_form_response_wrapper(
            user_id=user_id,
            form_id=form_id,
            question_id=question_id,
            presenter=presenter
        )

    # Assert
    assert actual_response_id == response_id
    storage.validate_form_id.assert_called_once_with(form_id=form_id)
    storage.validate_question_id.assert_called_once_with(
        question_id=question_id)
    storage.validate_question_id_with_form.assert_called_once_with(
        form_id=form_id, question_id=question_id)
    storage.get_option_ids_for_question.assert_called_once_with(
        question_id=question_id)
    storage.get_question_type.assert_called_once_with(question_id=question_id)
    storage.create_user_response.assert_called_once_with(
        user_id=user_id,
        question_id=question_id,
        user_submitted_response=user_submitted_response)
    presenter.submit_form_response_return.assert_called_once_with(
        response_id=response_id)
