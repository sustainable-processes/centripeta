from centripeta import Analyzer, Dispenser
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
a = Analyzer(mgr)
d = Dispenser(manager=mgr, pump_controller=pumps)

# Clip 1: all the pumps refilling 
# pumps.apply_command_to_all_pumps('go_to_max_volume')
# pumps.apply_command_to_all_pumps('go_to_volume',0)

# Clip 2: prepare samples
# Read in conditions and run the robot
# d.turn_wheel(n_turns=1)
# conditions = pd.read_csv('conditions/acetone_water_1.csv')
# for i, condition in conditions.iterrows():
#     logging.info("{Dipsensing condition %s"%i)
#     print('sample preparation')
#     d.dispense(pump_name="sample", volume =condition['sample']) 
#     d.dispense(pump_name="water", volume=condition['water'])
#     d.dispense(pump_name="acetone", volume=condition['acetone'])
    
#     print('next sample')
#     d.turn_wheel(n_turns=1)

# Clip 3: Conductivity test
# a.start_fans(50)
# a.cond_test()
# a.stop_fans()

# Clip 4: Turbidity test

a.turn_wheel(n_turns=3)
# a.turb_test()
# Clip 5: Take a picture
# import cv2

# camera = cv2.VideoCapture(0)
# for i in range(2):
#     return_value, image = camera.read()
#     cv2.imwrite('sample'+str(i)+'.png', image)
#     img = cv2.imread('sample'+str(i)+'.png')
#     cv2.namedWindow('sample'+str(i)+'.png')
#     cv2.imshow('sample'+str(i)+'.png', img)
#     cv2.waitKey (0)
#     a.turn_wheel(n_turns=1)
# del(camera)
# cv2.destroyAllWindows()