from centripeta import WheelControl
import json

with open('platform_config.json', 'r') as f:
    config = json.load(f)


w = WheelControl(config=config, wheel_name='dispenseWheel')
w.turn_wheel(5)