from centripeta import Dispenser
from pycont.controller import MultiPumpController
from commanduino import CommandManager
import json

    
mgr = CommandManager.from_configfile('platform_config_ports.json')
pump_ctrl = MultiPumpController.from_configfile('pycont_config.json')


d = Dispenser(mgr, pump_ctrl)
d.turn_wheel(n_turns=10)

