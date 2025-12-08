from django.apps import AppConfig


class Config(Config):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aero_facil'