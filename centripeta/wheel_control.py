"""
.. module:: wheel_control
    :platform: Unix
    :synopsis: Module for interfacing with the Commanduino core device in the Base Layer

.. moduleauthor:: Graham Keenan <https://github.com/ShinRa26>

"""

import os
import sys
import inspect
from .core_device import CoreDevice, CommanduinoInitError

""" CONSTANTS """
FULL_WHEEL_TURN = 6400
PUMP_INCREMENT = 8000
MODULE_LOWER = -39000


class WheelControl(CoreDevice):
    """
    Class for controlling a Geneva Wheel system
    Contains methods for rotation, modular drivers, pumps, etc.
    Assumes the user has at least one Geneva wheel, one modular driver, and one peristaltic
    pump attached to their rig.

    Inherits:
        CoreDevice: Commanduino Base Device

    Args:
        config (str): Dictionary contianing the configuration data.
    """
    def __init__(self, config, name):
        CoreDevice.__init__(self, config, name)
        if not self.mgr.devices:
            raise CommanduinoInitError("No devices found in the manager")

    def turn(self, n_turns, wait=True):
        """
        Turns the Geneva Wheel n_turns times

        Args:
            wheel_name (str): Name of the wheel to turn
            n_turns (int): Number of turns
        """
        drive_wheel = self.get_device_attribute()
        for _ in range(n_turns):
            drive_wheel.move(FULL_WHEEL_TURN, wait=wait)

    def home_module(self, wait=True):
        """
        Brings the module back to its home position
        """
        drive_wheel = self.get_device_attribute()
        drive_wheel.home(wait=wait)
