class DBRoutesWelding:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'spwm_welding':
            return 'welding'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'spwm_welding':
            return 'welding'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'spwm_welding' or \
           obj2._meta.app_label == 'spwm_welding':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'spwm_welding':
            return db == 'welding'
        return None


class DBRoutesPipeCleaning:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'spwm_pipe_cleaning':
            return 'pipecleaning'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'spwm_pipe_cleaning':
            return 'pipecleaning'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'spwm_pipe_cleaning' or \
           obj2._meta.app_label == 'spwm_pipe_cleaning':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'spwm_pipe_cleaning':
            return db == 'pipecleaning'
        return None


