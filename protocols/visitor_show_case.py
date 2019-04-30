"""
Testing for the control of pH_probe sequential movement

"""
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

# Read in conditions and run the robot
# conditions = pd.read_csv('conditions/acetone_water_1.csv')
# for i, condition in conditions.iterrows():
#     logging.info("{Dipsensing condition %s"%i)
#     print('sample preparation')
#     d.dispense(pump_name="sample", volume =condition['sample']) 
#     d.dispense(pump_name="acetone", volume=condition['acetone'])
#     d.dispense(pump_name="water", volume=condition['water'])
#     print('next sample')
#     d.turn_wheel(n_turns=1)
# time.sleep(5)
# explaining the role of robotic arm
# print('robotic arm for vial transfer')
# take a picture
import cv2
camera = cv2.VideoCapture(0)

for i in range(2):
    return_value, image = camera.read()
    cv2.imwrite('sample'+str(i)+'.png', image)
    img = cv2.imread('sample'+str(i)+'.png')
    cv2.namedWindow('sample'+str(i)+'.png')
    cv2.imshow('sample'+str(i)+'.png', img)
    cv2.waitKey (0)
    a.turn_wheel(n_turns=1)
del(camera)
cv2.destroyAllWindows()

a.start_fans(50)
print('cleaning station is working now')
a.cond_test()
a.turn_wheel(n_turns=1)
a.stop_fans()
print('Done:)')


