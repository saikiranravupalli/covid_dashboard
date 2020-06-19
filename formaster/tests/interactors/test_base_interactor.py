import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from formaster.interactors.storages.storage_interface import StorageInterface
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.exceptions.exceptions import FormDoesNotExist, FormClosed, \
    QuestionDoesNotExist, QuestionDoesNotBelongToForm
from formaster.interactors.submit_form_response.base import \
    BaseSubmitFormResponseInteractor

def test_base_interactor_with_invalid_form_id_raises_exception():
    # Arrange
    invalid_form_id = -1
    question_id = 1
    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = BaseSubmitFormResponseInteractor(
        storage=storage,
        question_id=question_id,
        form_id=invalid_form_id,
        user_id=user_id
    )
    storage.validate_form_id.side_effect = FormDoesNotExist
    presenter.raise_exception_for_form_does_not_exists.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.submit_form_response_wrapper(presenter=presenter)

    # Assert
    storage.validate_form_id.assert_called_once_with(form_id=invalid_form_id)
    presenter.raise_exception_for_form_does_not_exists.assert_called_once()

def test_base_interactor_with_invalid_question_id_raises_exception():
    # Arrange
    form_id = 1
    question_id = -1
    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = BaseSubmitFormResponseInteractor(
        storage=storage,
        question_id=question_id,
        form_id=form_id,
        user_id=user_id
    )
    storage.validate_question_id.side_effect = QuestionDoesNotExist
    presenter.raise_exception_for_question_does_not_exists.side_effect = \
        NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.submit_form_response_wrapper(presenter=presenter)

    # Assert
    storage.validate_form_id.assert_called_once_with(form_id=form_id)
    storage.validate_question_id.assert_called_once_with(
        question_id=question_id)
    presenter.raise_exception_for_question_does_not_exists.\
        assert_called_once()

def test_base_interactor_with_question_does_not_belong_to_form_raises_exception():
    # Arrange
    form_id = 1
    question_id = 1
    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = BaseSubmitFormResponseInteractor(
        storage=storage,
        question_id=question_id,
        form_id=form_id,
        user_id=user_id
    )
    storage.validate_question_id_with_form.side_effect = \
        QuestionDoesNotBelongToForm
    presenter.raise_exception_for_question_does_not_belong_to_form.\
        side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.submit_form_response_wrapper(presenter=presenter)

    # Assert
    storage.validate_form_id.assert_called_once_with(form_id=form_id)
    storage.validate_question_id.assert_called_once_with(
        question_id=question_id)
    storage.validate_question_id_with_form.assert_called_once_with(
        form_id=form_id, question_id=question_id)
    presenter.raise_exception_for_question_does_not_belong_to_form.\
        assert_called_once()

def test_base_interactor_with_form_closed_raises_exception():

    # Arrange
    form_id = 1
    question_id = 1
    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = BaseSubmitFormResponseInteractor(
        storage=storage,
        question_id=question_id,
        form_id=form_id,
        user_id=user_id
    )
    storage.validate_for_live_form.side_effect = FormClosed
    presenter.raise_exception_for_form_closed.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.submit_form_response_wrapper(presenter=presenter)

    # Assert
    storage.validate_form_id.assert_called_once_with(form_id=form_id)
    storage.validate_for_live_form.assert_called_once_with(
        form_id=form_id)
    presenter.raise_exception_for_form_closed.assert_called_once()
