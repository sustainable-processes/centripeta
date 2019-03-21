from centripeta import WheelControl
from commanduino import CommandManager
from commanduino.devices.axis import Axis, MultiAxis
import json

with open('platform_config.json', 'r') as f:
    wheel_config = json.load(f)

with open('platform_config_simple.json', 'r') as f:
    platform_config = json.load(f)
    
steppers = CommandManager.from_config(platform_config)
# w = WheelControl(config=wheel_config, name='analysisWheel')
# w.turn(3)



horzpH = steppers.devices['horzpH']

horzpH.home()

horzpH.move_to(10000)


