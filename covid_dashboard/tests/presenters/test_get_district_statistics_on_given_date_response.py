from covid_dashboard.presenters.presenter_implementation import \
    PresenterImplementation


def test_get_district_statistics_response_with_valid_details_returns_statistics_dict(
    district_statistics_dto, district_statistics_response):

    # Arrange
    presenter = PresenterImplementation()
    expected_dict = district_statistics_response

    # Act
    response = presenter.get_district_statistics_on_given_date_response(
        district_statistics_on_date_dto=district_statistics_dto
    )

    # Assert
    assert response == expected_dict
