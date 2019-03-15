"""
.. module:: tricont_control
    :platform: Unix, Windows
    :synopsis: Module for controlling Tricont pumps defined in the Base Layer

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

""" CONSTANTS """
GROUPS = "groups"
OUTPUT_PUMP = "sample" # Sample/waste/output pump - Call it whatever you want
WATER_PUMP = "water"
ACETONE_PUMP = "acetone"

# Assumes 4 way dist valves
INLET = "I"
OUTLET = "O"
EXTRA = "E"

# Assumes 6-way Valve
POS1 = "1"
POS2 = "2"
POS3 = "3"
POS4 = "4"
POS5 = "5"
POS6 = "6"

# Numerics
CLEAN_CYCLES = 2


class TricontControl(object):
    """
    Class for controlling a set of tricont pumps
    Contains methods for dispensing, sampling, cleaning vials, etc.
    """
    def __init__(self):
        from base_layer.tricont import triconts

        self.controller = triconts.controller
        self.config = triconts.config


    def get_tricont(self, pump_name):
        """
        Gets the Tricont pump attribute from the PyCont controller

        Args:
            pump_name (str): Name of the pump

        Returns:
            pump (C3000Controller): Pump object

        Raises:
            AttributeError: The pump is not present within the PyCont controller
        """
        try:
            return getattr(self.controller, pump_name)
        except AttributeError:
            print("Unable to locate pump {0} in PyCont controller!".format(pump_name))
            sys.exit(-1)


    def get_tricont_group(self, group_name):
        """
        Gets a group of tricont objects associated with a group in the PyCont config

        Args:
            group_name (str): Name of the pump group from the PyCont config

        Returns:
            pumps (Dict): Dictionary of the pump names and their associated PyCont objects
        """
        try:
            pumps = {}
            pump_group = self.config[GROUPS][group_name]
            for p in pump_group:
                pump = self.get_tricont(p)
                pumps[p] = pump

            return pumps
        except KeyError:
            print("Invalid pump group: {0}".format(group_name))
            sys.exit(-1)
            


    def transfer(self, name, vol, in_valve=INLET, out_valve=OUTLET, wait=True):
        """
        Waits until a pump is idle before transferring a volume
        
        Args:
            name (str): Name of the pump
            vol (int/float): Volume to transfer
            in_valve (str): Valve to pull from to
            out_valve (str): Valve to push towards
            wait (bool): Wait for the pump to be idle, default set to True
        """
        pump = self.get_tricont(name)

        if wait:
            pump.wait_until_idle()
            pump.transfer(vol, in_valve, out_valve)
        else:
            # TODO: CHECK VOLUMES DONT CAUSE PROBLEMS BUT I KNOW THEY PROBABLY WILL
            pump.pump(vol, in_valve, wait=True)
            pump.deliver(vol, out_valve)


    def dispense_reagents(self, reagents):
        """
        Dispenses reagents from their stock solutions to a vessel

        Args:
            reagents (Dict): Dictionary containing pump names and values to transfer
        """
        for name, value in reagents.items():
            self.transfer(name, value, INLET, OUTLET) # Assumes 4-way valve, change as appropriate

    
    def output(self, volume):
        """
        Calls on the sample/waste line to take a sample out of a vessel
        Change as needed.

        Args:
            volume (int/float): Volume to remove
        """
        self.transfer(OUTPUT_PUMP, volume, INLET, OUTLET) # Assumes 4-way valve, change as appropriate


    def clean_routine(self):
        """
        Cleans out a vial with the water and acetone pumps
        Change as required
        """
        for _ in range(CLEAN_CYCLES):
            self.transfer(WATER_PUMP, 12.5)
            self.transfer(OUTPUT_PUMP, 25)
            self.transfer(WATER_PUMP, 12.5)
            self.transfer(OUTPUT_PUMP, 25)
            self.transfer(ACETONE_PUMP, 6)
            self.transfer(OUTPUT_PUMP, 25)
            self.transfer(WATER_PUMP, 5)
            self.transfer(OUTPUT_PUMP, 12.5)
            self.transfer(WATER_PUMP, 12.5)
            self.transfer(OUTPUT_PUMP, 12.5)
            self.transfer(WATER_PUMP, 12.5)
            self.transfer(OUTPUT_PUMP, 25)


    """
    ADD ANY ADDITIONAL FUNCTIONALITY BELOW AS REQUIRED
    """