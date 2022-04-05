from django.apps import AppConfig

# copy the following app name (as a string) to add it in settings.py
class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
