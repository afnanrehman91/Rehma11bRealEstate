from django.apps import AppConfig


class EpropertyConfig(AppConfig):
    name = 'eproperty'

    def ready(self):
        import eproperty.signals
