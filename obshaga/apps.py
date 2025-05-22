from django.apps import AppConfig

class ObshagaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'obshaga'

    def ready(self):
        from django.conf import settings
        if settings.SCHEDULER_SHOULD_RUN:
            from .scheduler import start_scheduler_job
            start_scheduler_job()