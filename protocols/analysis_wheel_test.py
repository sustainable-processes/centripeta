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

#Read in the configuration files
with open('platform_config_simple.json', 'r') as f:
    config = json.load(f)

w = WheelControl(config=config, name="analysisWheel")
steppers = CommandManager.from_config(config)
c = Analyzer(wheel=w, steppers=steppers)

# c.turn_wheel(n_turns=5)
print("turning wheel")
c.horzpH_move_to(steps=20000)

