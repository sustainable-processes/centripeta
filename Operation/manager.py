from centripeta import Centripeta, WheelControl, Tricont
import json

with open('platform_config.json', 'r') as f:
    wheel_config = json.load(f)

with open('pycont_config.json', 'r') as f:
    pump_config = json.load(f)

w = WheelControl(config=wheel_config, name="dispenseWheel")
pumps = Tricont(config=pump_config, name="")

c = Centripeta(wheel=w, pumps=pumps)

c.dispense()