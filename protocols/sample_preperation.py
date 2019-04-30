from centripeta import Dispenser
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
pumps = MultiPumpController.from_configfile('pycont_config.json')
d = Dispenser(manager=mgr, pump_controller=pumps)

d.turn_wheel(n_turns=1)
#Read in conditions and run the robot
conditions = pd.read_csv('conditions/xp_initial_0.csv')
for i, condition in conditions.iterrows():
    logging.info("{Dipsensing condition %s"%i)
    d.dispense(pump_name="Texapon", volume =condition['Texapon']) 
    d.dispense(pump_name="DehytonAB30", volume=condition['DehytonAB30'])
    d.dispense(pump_name="Plantacare818", volume=condition['Plantacare818'])
    d.dispense(pump_name="CC7BZ", volume=condition['CC7BZ'])
    d.dispense(pump_name="ArlyponTT", volume=condition['ArlyponTT'])
    d.dispense(pump_name="water", volume=condition['water'])
    d.turn_wheel(n_turns=1)
    print('finish sample' + 'i')

print('completed')