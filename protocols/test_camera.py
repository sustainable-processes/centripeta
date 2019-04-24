import os

# this get our current location in the file system
import inspect
HERE_PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

# adding parent directory to path, so we can access the utils easily
import sys
root_path = os.path.join(HERE_PATH, '..', '..')
sys.path.append(root_path)

import cv2
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
a = Analyzer(mgr)

camera = cv2.VideoCapture(1)

for i in range(24):
    return_value, image = camera.read()
    cv2.imwrite('opencv'+str(i)+'.png', image)
    a.turn_wheel(n_turns=1)
del(camera)

