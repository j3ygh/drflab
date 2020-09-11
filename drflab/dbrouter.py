from django.conf import settings


class DBRouter:
    """
    DEFAULT_APPS --> default
    CUSTOME_APPS --> custom
    """
    DEFAULT_APPS = settings.DEFAULT_APPS
    CUSTOM_APPS = settings.CUSTOM_APPS
    default_database = 'default'
    custom_database = 'custom'

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.DEFAULT_APPS:
            return self.default_database
        return self.custom_database

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.DEFAULT_APPS:
            return self.default_database
        return self.custom_database

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        print(self.DEFAULT_APPS)
        print(self.CUSTOM_APPS)
        if app_label in self.DEFAULT_APPS:
            if db == self.default_database:
                return True
        if app_label in self.CUSTOM_APPS:
            if db == self.custom_database:
                return True
        return None
