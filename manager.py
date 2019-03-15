"""
.. module:: manager
    :platform: Unix
    :synopsis: Module for managing the Operational layer components

.. moduleauthor:: Graham Keenan <https://github.com/ShinRa26>

"""

import os
import sys
import inspect
import logging 

HERE = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
root_path = os.path.join(HERE, "..")
sys.path.append(root_path)

""" Operations Modules """
# Add more as required
from operations.triconts.tricont_control import TricontControl
from operations.wheel.wheel_control import WheelControl
from operations.camera.camera_control import CameraControl

""" Constants """
OP_CONFIGS = os.path.join(HERE, "operations", "configs")
WHEEL_CONFIG = os.path.join(OP_CONFIGS, "platform_config.json")

# Numeric constants
WHEEL_TURN = 1


class Manager(object):
    """
    Class representing a manager which governs the entire platform
    Wrapper around certain operations for the platform and general management

    """
    def __init__(self):

        # Initialise the camera
        self.camera = CameraControl()

        # Initialise the tricont pumps
        self.triconts = TricontControl()

        # Initialise the Wheel system
        self.wheel = WheelControl(WHEEL_CONFIG)

        # Initialise the logging module
        self.logger = Logger()

    def dispense(self, wheel_name, reagents):
        """
        Dispenses reagents into a vial and rotates the wheel

        Args:
            reagents (Dict): Dictionary containing the pump names and values
        """
        for pump, vol in reagents.keys():
            self.triconts.transfer(pump, vol)

        self.turn_wheel(wheel_name, WHEEL_TURN)


    def dispense_single_reagent(self, name, volume):
        """
        Dispenses a single reagent from the pump

        Args:
            name (str): Name of the reagent pump
            volume (int/float): Volume to dispense
        """
        self.triconts.transfer(name, volume)

    
    def turn_wheel(self, wheel_name, n_turns):
        """
        Turns the wheel n_turns times

        Args:
            n_turns (int): Number of times to turn the wheel
        """
        self.wheel.turn_wheel(wheel_name, n_turns)

    
    def log(self, msg):
        """
        Logs a message using the logger

        Args:
            msg (str): Message to log
        """
        self.logger.info(msg)



