from django.conf import settings


class DBRouter:
    """
    DEFAULT_APPS --> default_database
    CUSTOME_APPS --> custom_database
    """
    DEFAULT_APPS = settings.DEFAULT_APPS
    CUSTOM_APPS = settings.CUSTOM_APPS
    default_database = 'default_database'
    custom_database = 'custom_database'

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.DEFAULT_APPS:
            return self.default_database
        return self.custom_database

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.DEFAULT_APPS:
            return self.default_database
        return self.custom_database

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True
