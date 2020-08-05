import os
import sys


class Config(object):
    """Configuration variables for this test suite

    This creates a variable named CONFIG (${CONFIG} when included
    in a test as a variable file.

    Example:

    *** Settings ***
    | Variable | ../resources/config.py

    *** Test Cases ***
    | Example
    | | log | username: ${CONFIG}.username
    | | log | root url: ${CONFIG}.root_url

    """

    def __init__(self):
        _here = os.path.dirname(__file__)

        sys.path.insert(0, os.path.abspath(os.path.join(_here, "..", "..")))
        sys.path.insert(0, os.path.abspath(os.path.join(_here)))

        # self.demo_root = os.path.abspath(os.path.join(_here, ".."))
        # self.port = 8000
        self.base_url = "https://demoqa.com"
        self.first_name = "Jonathan"
        self.last_name = "Hernandez"
        self.email = "hernandezj84@gmail.com"
        self.number = "9999999999"
        self.date_of_birth = "24 Apr 1984"

        # self.username = "test user"
        # self.password = "password"

    def __str__(self):
        return "<Config: %s>" % str(self.__dict__)


# This creates a variable that robot can see
CONFIG = Config()
