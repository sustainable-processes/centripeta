"""
.. module:: wheel_control
    :platform: Unix
    :synopsis: Module for interfacing with the Commanduino core device in the Base Layer

.. moduleauthor:: Graham Keenan <https://github.com/ShinRa26>

"""

import os
import sys
import inspect

HERE = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
root_path = os.path.join(HERE, "..", "..")
op_path = os.path.join(HERE, "..")
sys.path.append(op_path)
sys.path.append(root_path)

from base_layer.commanduino_setup.core_device import CoreDevice
from base_layer.commanduino_setup.core_device import CommanduinoInitError

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
        config (str): Path to the config
    """
    def __init__(self, config):
        CoreDevice.__init__(self, config)
        if not self.mgr.devices:
            raise CommanduinoInitError("No devices found in the manager")


    def turn_wheel(self, wheel_name, n_turns, wait=True):
        """
        Turns the Geneva Wheel n_turns times

        Args:
            wheel_name (str): Name of the wheel to turn
            n_turns (int): Number of turns
        """
        drive_wheel = self.get_device_attribute(wheel_name)
        for _ in range(n_turns):
            drive_wheel.move(FULL_WHEEL_TURN, wait=wait)


    def move_module(self, mod_name, pos, wait=True):
        """
        Moves the modular driver to a set position

        Args:
            mod_name (str): Name of the module
            pos (int/float): Number of steps to move
            wait (bool): Wait for the device to be idle, default set to True
        """
        module = self.get_device_attribute(mod_name)
        module.move(-pos, wait=wait) # -ve due to inverted direction


    def lower_module(self, mod_name, wait=True):
        """
        Lowers the modular driver

        Args:
            mod_name (str): Name of the modular driver
            wait (bool): Wait for the device to be idle, default set to true
        """
        self.move_module(mod_name, MODULE_LOWER, wait=wait)


    def home_module(self, mod_name, wait=True):
        """
        Brings the module back to its home position

        Args:
            mod_name (str): Name of the module
            wait (bool): Wait for the device to be idle, default set to true
        """
        module = self.get_device_attribute(mod_name)
        module.home(wait=wait)


    def set_pwm(self, mod_name, value):
        """Sets the pwm value for items attached to MOSFET units

        Arguments:
            mod_name {str} -- Name of the attached module
            value {int} -- Value to set (0-255)
        """
        if self.valid_device(mod_name):
            mod = self.get_device_attribute(mod_name)
            mod.set_pwm_value(value)
        else:
            print('"{}" is not recognised in the manager!'.format(mod_name))
