from covid_dashboard.presenters.presenter_implementation import \
    PresenterImplementation


def test_get_day_wise_statistics_response_with_valid_details_returns_statistics_dict(
    district_day_wise_statistics_dtos, district_day_wise_statistics_response):

    # Arrange
    presenter = PresenterImplementation()
    expected_dict = district_day_wise_statistics_response

    # Act
    response = presenter.get_day_wise_district_statistics_response(
        day_wise_district_statistics_dtos=district_day_wise_statistics_dtos
    )

    # Assert
    assert response == expected_dict
