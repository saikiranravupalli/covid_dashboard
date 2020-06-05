from covid_dashboard.presenters.presenter_implementation import \
    PresenterImplementation


def test_get_state_statistics_response_with_valid_details_returns_statistics_dict(
    state_statistics_dto, state_statistics_response):

    # Arrange
    presenter = PresenterImplementation()
    expected_dict = state_statistics_response

    # Act
    response = presenter.get_state_statistics_on_given_date_response(
        state_statistics_dto=state_statistics_dto
    )

    # Assert
    assert response == expected_dict
