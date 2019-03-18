"""
Dispensing for acetone and water

"""
from centripeta import Dispenser, WheelControl
from pycont.controller import MultiPumpController
import json
import pandas as pd
import logging

#Read in the configuration files
with open('platform_config.json', 'r') as f:
    wheel_config = json.load(f)

with open('pycont_config.json', 'r') as f:
    pump_config = json.load(f)

#Instantiate the robotic controls
w = WheelControl(config=wheel_config, name="dispenseWheel")
pumps = MultiPumpController(config=pump_config)
c = Dispenser(wheel=w, pumps=pumps)

#Read in conditions and run the robot
conditions = pd.read_csv('conditions/acetone_water_1.csv')
for i, condition in enumerate(conditions.iterrows()):
    logging.info(f"{Dipsensing condition {i}}")
    c.dispense(pump_name="sample", volume = conditions['sample'] )
    c.dispense(pump_name="acetone", volume=conditions['acetone'])
    c.dispense(pump_name="water", volume=conditions['water'])
    c.turn_wheel(n_turns=1)