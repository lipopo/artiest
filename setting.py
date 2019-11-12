import os


class Setting(object):
    @property
    def db_url(self):
        return os.environ.get('DATABASE')


setting = Setting()

