from covid_dashboard.presenters.presenter_implementation import \
    PresenterImplementation


def test_get_district_day_wise_cumulative_statistics_response_with_valid_details_returns_cumulative_dict(
    districts_day_wise_dtos, day_wise_district_cumulative_response):

    # Arrange
    presenter = PresenterImplementation()
    expected_dict = day_wise_district_cumulative_response

    # Act
    response = \
        presenter.get_day_wise_districts_cumulative_statistics_response(
            day_wise_districts_cumulative_dtos=districts_day_wise_dtos
        )

    # Assert
    assert response == expected_dict
