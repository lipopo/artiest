import os

import yaml


pwd_folder = os.path.dirname(__file__)


class Setting(object):
    _website_setting = {}


    @property
    def db_url(self):
        return os.environ.get('DATABASE')

    @property
    def website_setting(self):
        # if not self._website_setting:
        self._website_setting = yaml.load(open(os.path.join(pwd_folder, 'website.yml')))
        return self._website_setting

setting = Setting()

