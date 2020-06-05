from covid_dashboard.presenters.presenter_implementation import \
    PresenterImplementation


def test_get_day_wise_cumulative_statistics_response_with_valid_details_returns_cumulative_dict(
    district_day_wise_dto, district_cumulative_response):

    # Arrange
    presenter = PresenterImplementation()
    expected_dict = district_cumulative_response

    # Act
    response = presenter.get_day_wise_district_cumulative_statistics_response(
        day_wise_district_cumulative_dto=district_day_wise_dto
    )

    # Assert
    assert response == expected_dict
