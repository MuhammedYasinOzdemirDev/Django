from django.apps import AppConfig

#uygulama ismi belirlenir
class ArticleConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "article"
