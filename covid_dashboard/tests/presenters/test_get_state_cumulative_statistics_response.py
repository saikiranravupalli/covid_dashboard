from covid_dashboard.presenters.presenter_implementation import \
    PresenterImplementation


def test_get_state_cumulative_statistics_response_with_valid_details_returns_cumulative_dict(
    state_stats_dto, state_cumulative_response):

    # Arrange
    presenter = PresenterImplementation()
    expected_dict = state_cumulative_response

    # Act
    response = presenter.get_state_cumulative_statistics_response(
        state_cumulative_statistics_dto=state_stats_dto
    )

    # Assert
    assert response == expected_dict
