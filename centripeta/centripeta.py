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
from commanduino import CommandManager

class Centripeta:
    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def from_config(cls, config):
        return cls(config)

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
        self._mgr = pumps
        self._mgr.smart_initialize()
        self.pumps = self._mgr.pumps 

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
        self.pumps[pump_name].pump(volume, 'I')
        self.pumps[pump_name].deliver(volume, 'O')

    def turn_wheel(self, n_turns):
        """
        Turn the wheel n_turns

        Args:
            n_turns (int): Number of turns to rotate the wheel
        """
        self.wheel.turn(n_turns, wait=True)

class Analyzer(Centripeta):
    """
    Control of a analysis wheel 
    Attributes:
        wheel (centripeta.WheelControl): A WheelControl object from centripeta
    """

    def __init__(self, wheel: WheelControl, steppers: CommandManager):
        
        # Initialize the wheel system
        # self.wheel = wheel

        # Initialize the linear accelsteppers
        self.mgr = steppers

        self.horzpH = self.mgr.devices['horzpH']
        # self.vertpH = self.mgr.devices['vertpH']
        self.wheel = self.mgr.devices['Analysiswheel']

    def turn_wheel(self, n_turns):
        """
        Turn the wheel n_turns

        Args:
            n_turns (int): Number of turns to rotate the wheel
        """
        self.wheel.turn(n_turns, wait=True)
    
    def horzpH_move_to(self, steps, wait=True):
        """
        Move the stepmoter to a specific location

        Args:
            steps (int): The position to move to 
            wait (bool): Wait until the device is idle, defualt set to True

        """
        self.horzpH.move_to(steps)

    def move_to(self, name, steps):
        self.mgr.devices[name].move_to(steps)