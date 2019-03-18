"""
.. module:: manager
    :platform: Unix
    :synopsis: Module for managing the Operational layer components

.. moduleauthor:: Kobi Felton <https://github.com/marcosfelt>

"""

import os
import sys
import inspect
import logging 

# Add more as required
from pycont.controller import MultiPumpController
from .wheel_control import WheelControl

class Centripeta:
    def __init__(self):
        pass

class Dispenser(Centripeta):
    """
    Control of a dispensing wheel that has an arbitrary number of pumps connected.

    Attributes:
        wheel (centripeta.WheelControl): A WheelControl object from centripeta
        pumps (pycont.controller.MultiPumpController): A MultiPumpController object for all the pump
            connected to the wheel

    """
    def __init__(self, wheel: WheelControl, pumps: MultiPumpController=None):

        # Initialise the camera
        # self.camera = CameraControl()

        # Initialise the tricontinental pumps
        self.pumps = pumps
        self.pumps.smart_initialize()

        # Initialise the Wheel system
        self.wheel = wheel

        # # Initialise the logging module
        # self.logger = Logger())


    def dispense(self, pump_name, volume):
        """
        Dispenses a single reagent from the pump

        Args:
            name (str): Name of the reagent pump
            volume (int/float): Volume to dispense
        """
        self.pumps[pump_name].transfer(volume, 'I', 'O')

    def turn_wheel(self, n_turns):
        """
        Turn the wheeel n_turns

        Args:
            n_turns (int): Number of turns to rotate the wheel
        """
        self.wheel.turn(n_turns, wait=True)



