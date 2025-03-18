from django.apps import AppConfig

class CrudConfig(AppConfig):
    # Define la configuración de la aplicación 'crud'
    default_auto_field = 'django.db.models.BigAutoField'  # Especifica el campo de clave primaria predeterminado
    name = 'crud'  # Nombre de la aplicación dentro del proyecto Django