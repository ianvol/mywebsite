from django.apps import AppConfig

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'  # Change this to your desired default auto field
    name = 'app'  # Change this to your app's name

