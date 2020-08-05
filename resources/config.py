import os
import sys


class Config(object):

    def __init__(self):
        _here = os.path.dirname(__file__)

        sys.path.insert(0, os.path.abspath(os.path.join(_here, "..", "..")))
        sys.path.insert(0, os.path.abspath(os.path.join(_here)))

        self.base_url = "https://demoqa.com"
        self.first_name = "Jonathan"
        self.last_name = "Hernandez"
        self.email = "hernandezj84@gmail.com"
        self.number = "9999999999"
        self.date_of_birth = "24 Apr 1984"

    def __str__(self):
        return "<Config: %s>" % str(self.__dict__)

CONFIG = Config()
