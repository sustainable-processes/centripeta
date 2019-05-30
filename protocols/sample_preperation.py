from centripeta import Dispenser
from centripeta.utils import Logger
from pycont.controller import MultiPumpController
from commanduino import CommandManager
import pandas as pd
import logging
import time

# Set up logger
logging.basicConfig(filename='log.txt', level=logging.INFO)
logger = logging.getLogger(__name__)

#Instantiate the command manager
mgr = CommandManager.from_configfile('platform_config_ports.json')
pumps = MultiPumpController.from_configfile('pycont_config.json')
d = Dispenser(manager=mgr, pump_controller=pumps)

# d.home_wheel()
# time.sleep(5)
# d.turn_wheel(n_turns=2)

# Read in conditions and run the robot
conditions = pd.read_csv('conditions/xp_test.csv')
for i, condition in conditions.iterrows():
    logging.info("{Dipsensing condition %s"%i)
    d.dispense(pump_name="Texapon", volume =condition['Texapon'], speed_in=1500) 
    d.dispense(pump_name="DehytonAB30", volume=condition['DehytonAB30'], speed_in=1500)
    d.dispense(pump_name="Plantacare818", volume=condition['Plantacare818'], speed_in=1500)
    d.dispense(pump_name="DehytonPK45", volume=condition['DehytonPK45'])
    d.dispense(pump_name="DehytonMC", volume=condition['DehytonMC'], speed_in=1000)
    d.dispense(pump_name="Plantacare2000", volume=condition['Plantacare2000'], speed_in=1500)
    d.dispense(pump_name="PlantaponLGCsorb", volume=condition['PlantaponLGCsorb'], speed_in=400)
    d.dispense(pump_name="ArlyponTT", volume=condition['ArlyponTT'])
    d.dispense(pump_name="CC7BZ", volume=condition['CC7BZ'])
    time.sleep(10)
    d.dispense(pump_name="water", volume=condition['water'])
    d.turn_wheel(n_turns=1)
    print('finish sample' + 'i')

print('completed')