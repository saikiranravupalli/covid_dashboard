from covid_dashboard.presenters.presenter_implementation import \
    PresenterImplementation


def test_get_district_cumulative_statistics_response_with_valid_details_returns_cumulative_dict(
    district_cumulative_statistics_dto, district_cumulative_statistics_response):

    # Arrange
    presenter = PresenterImplementation()
    expected_dict = district_cumulative_statistics_response

    # Act
    response = presenter.get_district_cumulative_statistics_response(
        district_cumulative_statistics_dto=district_cumulative_statistics_dto
    )

    # Assert
    assert response == expected_dict
