"""
.. module:: core_device
    :platform: Unix, Windows
    :synopsis: Baseline Commanduino implementation for primed Arduino boards

.. moduleauthor:: Graham Keenan <https://github.com/ShinRa26>

"""

import os
import sys
import json
import time
import inspect

from commanduino import CommandManager
from centripeta.utils import json_utils

""" CONSTANTS """
DEVICES = "devices"


class CommanduinoInitError(Exception):
    """
    Exception for errors when initialising commanduino
    """
    pass


class CoreDevice(object):
    """
    Class representing a core Commanduino system.
    Allows access to the modules attached

    Args:
        config (Dict): Dictionary containing the configuration data.
        name (str): Name of the device as specified in the config dictionary
    """
    def __init__(self, config, name):
        self.mgr = CommandManager.from_config(config)
        self.config = config
        self._name = name

    @property
    def name(self):
        return self._name

    def _valid_device(self):
        """
        Checks if the device name is present within the config

        Args:
            dev_name (str): name of the device

        Returns:
            valid (bool): If the device is present or not
        """
        return self.dev_name in self.config[DEVICES].keys()

    def get_device_attribute(self):
        """
        Gets the device attribute from CommandManager

        Args:
            dev_name (str): Name of the device

        Returns:
            device (CommandDevice): Device instance in the CommandManager

        Raises:
            AttributeError: The device is not in the CommandManager
        """
        if self._valid_device():
            try:
                return getattr(self.mgr, self.name)
            except AttributeError:
                print("No device named {0} in the manager!\nBailing out!".format(self.name))
                sys.exit(-1)
        else:
            print("Invalid device name: {0}".format(self.name))
            sys.exit(-1)
