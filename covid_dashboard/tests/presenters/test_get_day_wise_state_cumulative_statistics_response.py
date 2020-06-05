from covid_dashboard.presenters.presenter_implementation import \
    PresenterImplementation


def test_get_day_wise_cumulative_statistics_response_with_valid_details_returns_cumulative_dict(
    state_day_wise_cumulative_dto, day_wise_state_cumulative_response):

    # Arrange
    presenter = PresenterImplementation()
    expected_dict = day_wise_state_cumulative_response

    # Act
    response = presenter.get_day_wise_state_cumulative_statistics_response(
        day_wise_state_cumulative_dtos=state_day_wise_cumulative_dto
    )

    # Assert
    assert response == expected_dict
