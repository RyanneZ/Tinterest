from django.apps import AppConfig


class MainAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_app'


#Profile
class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals