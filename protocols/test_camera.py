from centripeta import Analyzer, Dispenser
from centripeta.utils import Logger
from pycont.controller import MultiPumpController
from commanduino import CommandManager
import pandas as pd
import logging
import time

import cv2

# Set up logger
logging.basicConfig(filename='log.txt', level=logging.INFO)
logger = logging.getLogger(__name__)

#Instantiate the command manager
mgr = CommandManager.from_configfile('platform_config_ports.json')
a = Analyzer(mgr)

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

