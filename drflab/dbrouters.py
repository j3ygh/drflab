class DBRouter:
    builtin_apps = {'admin', 'auth', 'contenttypes', 'sessions', 'messages', 'staticfiles'}
    custom_apps = {'rest_framework', 'api', 'crm', 'usage'}

    def db_for_read(self, model, **hints):
        return 'builtin' if model._meta.app_label in self.builtin_apps else 'custom'

    def db_for_write(self, model, **hints):
        return 'builtin' if model._meta.app_label in self.builtin_apps else 'custom'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.builtin_apps and db == 'builtin':
            result = True
        elif app_label in self.custom_apps and db == 'custom':
            result = True
        else:
            result = False
        return result
