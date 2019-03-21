"""
Testing for the control of the analysis wheel

"""
from centripeta import Analyzer, WheelControl
from centripeta.utils import Logger
from pycont.controller import MultiPumpController
from commanduino import CommandManager
import json
import pandas as pd
import logging

# Set up logger
logging.basicConfig(filename='log.txt', level=logging.INFO)
logger = logging.getLogger(__name__)

mgr = CommandManager.from_configfile('platform_config_simple.json')
c = Analyzer(mgr)

# c.turn_wheel(n_turns=5)
print("turning wheel")
c.horzpH_move_to(steps=20000)

