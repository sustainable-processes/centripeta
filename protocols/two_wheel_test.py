"""
Testing for the control of pH_probe sequential movement

"""
from centripeta import Analyzer, WheelControl, Dispenser
from centripeta.utils import Logger
from pycont.controller import MultiPumpController
from commanduino import CommandManager
import json
import pandas as pd
import logging

# Set up logger
logging.basicConfig(filename='log.txt', level=logging.INFO)
logger = logging.getLogger(__name__)

# testing the analysis wheel
mgr = CommandManager.from_configfile('platform_config_ports.json')
c = Analyzer(mgr)

c.turn_wheel(n_turns=3)
c.move('horz_cond', 10000)
c.home('horz_cond')
c.move('vert_cond', 10000)
c.home('vert_cond')

# tesing the preparation wheel

from centripeta import Dispenser, WheelControl
from pycont.controller import MultiPumpController

#Read in the configuration files

with open('pycont_config.json', 'r') as f:
    pump_config = json.load(f)

# Instantiate the robotic controls 
# w = WheelControl(config=wheel_config, name="dispenseWheel")
w = CommandManager.from_configfile('platform_config.json')
pumps = MultiPumpController(pump_config)
c = Dispenser(manager=w, pumps=pumps)

#Read in conditions and run the robot
conditions = pd.read_csv('conditions/acetone_water_1.csv')
for i, condition in conditions.iterrows():
    logging.info("{Dipsensing condition %s"%i)
    c.dispense(pump_name="sample", volume =condition['sample']) 
    c.dispense(pump_name="acetone", volume=condition['acetone'])
    c.dispense(pump_name="water", volume=condition['water'])
    c.turn_wheel(n_turns=1)