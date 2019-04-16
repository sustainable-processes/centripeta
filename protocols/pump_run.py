"""
Testing pumps with water

"""
from centripeta import Analyzer, Dispenser
from centripeta.utils import Logger
from pycont.controller import MultiPumpController
from commanduino import CommandManager
import pandas as pd
import logging

# Set up logger
logging.basicConfig(filename='log.txt', level=logging.INFO)
logger = logging.getLogger(__name__)

#Instantiate the command manager
mgr = CommandManager.from_configfile('platform_config_ports.json')
import pdb; pdb.set_trace()
pumps = MultiPumpController.from_configfile('pycont_config.json')
a = Analyzer(mgr)
d = Dispenser(manager=mgr, pump_controller=pumps)

d.dispense(pump_name="water", volume = 0.5)

# d.home_wheel()
# print("homing")


d.dispense(pump_name="acetone", volume=5)
# d.turn_wheel(5)

#Read in conditions and run the robot
# conditions = pd.read_csv('conditions/acetone_water_1.csv')
# for i, condition in conditions.iterrows():
#     logging.info("{Dipsensing condition %s"%i)
#     # d.dispense(pump_name="sample", volume =condition['sample']) 
#     d.dispense(pump_name="acetone", volume=condition['acetone'])
#     d.dispense(pump_name="water", volume=condition['water'])
#     d.turn_wheel(n_turns=1)