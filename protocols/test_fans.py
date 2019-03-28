from centripeta import Analyzer
from pycont.controller import MultiPumpController
from commanduino import CommandManager
import time
#Instantiate the command manager
mgr = CommandManager.from_configfile('platform_config_ports.json')
pumps = MultiPumpController.from_configfile('pycont_config.json')
a = Analyzer(mgr)

a.start_fans(100)
time.sleep(10)
a.stop_fans()

# sleep_time = 10
# a.drying_fans.set_pwm_value(0)
# a.a2_fans.set_pwm_value(0)
# time.sleep(5)
# a.drying_fans.set_pwm_value(150)
# a.a2_fans.set_pwm_value(150)
# print(f"Running fan for {sleep_time} seconds.")
# time.sleep(sleep_time)

# for i in range(1000):
#     a.drying_fans.set_pwm_value(255)
#     time.sleep(sleep_time)
#     a.drying_fans.set_pwm_value(0)
#     time.sleep(sleep_time)
#     a.drying_fans.set_pwm_value(50)
#     time.sleep(sleep_time)
#     a.drying_fans.set_pwm_value(0)
#     time.sleep(sleep_time)
