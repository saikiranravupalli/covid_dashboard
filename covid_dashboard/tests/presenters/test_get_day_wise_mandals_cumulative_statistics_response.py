from covid_dashboard.presenters.presenter_implementation import \
    PresenterImplementation


def test_get_day_wise_cumulative_statistics_response_with_valid_details_returns_cumulative_dict(
    mandals_day_wise_cumulative_stats, day_wise_mandals_cumulative_response):

    # Arrange
    presenter = PresenterImplementation()
    expected_dict = day_wise_mandals_cumulative_response

    # Act
    response = presenter.get_day_wise_mandals_cumulative_statistics_response(
        day_wise_mandals_cumulative_dtos=mandals_day_wise_cumulative_stats
    )

    # Assert
    assert response == expected_dict
