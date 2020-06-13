from django.apps import AppConfig


class EssentialsKitAppConfig(AppConfig):
    name = "essentials_kit"

    def ready(self):
        from essentials_kit import signals # pylint: disable=unused-variable
