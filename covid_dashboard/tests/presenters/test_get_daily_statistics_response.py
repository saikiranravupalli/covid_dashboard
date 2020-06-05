from covid_dashboard.presenters.presenter_implementation import \
    PresenterImplementation


def test_get_daily_statistics_response_with_valid_details_returns_statistics_dict(
    get_daily_statistics_dtos, get_daily_statistics_response):

    # Arrange
    presenter = PresenterImplementation()
    expected_dict = get_daily_statistics_response

    # Act
    response = presenter.get_daily_statistics_response(
        daily_statistics_dtos=get_daily_statistics_dtos
    )

    # Assert
    assert response == expected_dict
