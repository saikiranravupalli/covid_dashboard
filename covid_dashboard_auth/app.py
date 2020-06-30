from django.apps import AppConfig


class CovidDashboardAuthAppConfig(AppConfig):
    name = "covid_dashboard_auth"

    def ready(self):
        from covid_dashboard_auth import signals # pylint: disable=unused-variable
