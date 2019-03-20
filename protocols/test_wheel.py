from centripeta import WheelControl
from commanduino import CommandManager
from commanduino.devices.axis import Axis, MultiAxis
import json

with open('platform_config.json', 'r') as f:
    wheel_config = json.load(f)


w = WheelControl(config=wheel_config, name='analysisWheel')
w.turn(3)

steppers = CommandManager.from_configfile('platform_config.json')

horzpH = steppers.devices['horzpH']

horzpH.set_current_position(0)

horzpH.move_to(10000)


