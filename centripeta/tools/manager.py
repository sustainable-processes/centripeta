"""
.. module:: manager
    :platform: Unix
    :synopsis: Module for managing the Operational layer components

.. moduleauthor:: Graham Keenan <https://github.com/ShinRa26>

"""

import os
import sys
import inspect

HERE = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
root_path = os.path.join(HERE, "..")
sys.path.append(root_path)

""" Operations Modules """
# Add more as required
from operations.tricont_control import TricontControl
from operations.wheel_control import WheelControl

""" Constants """
OP_CONFIGS = os.path.join(HERE, "operations", "configs")
WHEEL_CONFIG = os.path.join(OP_CONFIGS, "wheel_config.json")



class Manager(object):
    """
    Class representing a manager which governs the entire platform
    Wrapper around certain operations for the platform and general management
    """
    def __init__(self):
        pass
