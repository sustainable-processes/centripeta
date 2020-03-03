import ctypes
import time
from picosdk.usbDrDaq import usbDrDaq as drDaq
import numpy as np
import matplotlib.pyplot as plt
from picosdk.functions import adc2mV, assert_pico_ok

def pH_test(test_time, sample_number):
    # Create chandle and status ready for use
    status = {}
    chandle = ctypes.c_int16()

    # Opens the device
    status["openunit"] = drDaq.UsbDrDaqOpenUnit(ctypes.byref(chandle))
    assert_pico_ok(status["openunit"])

    # Set sample interval
    us_for_block = ctypes.c_int32(test_time)
    ideal_no_of_samples = sample_number
    channels = ctypes.c_int32(drDaq.USB_DRDAQ_INPUTS["USB_DRDAQ_CHANNEL_PH"])
    no_of_channels = 1
    status["setInterval"] = drDaq.UsbDrDaqSetInterval(chandle, ctypes.byref(us_for_block), ideal_no_of_samples, ctypes.byref(channels), no_of_channels)
    assert_pico_ok(status["setInterval"])

    # Find scaling information
    channel = drDaq.USB_DRDAQ_INPUTS["USB_DRDAQ_CHANNEL_PH"]
    nScales = ctypes.c_int16(0)
    currentScale = ctypes.c_int16(0)
    names = (ctypes.c_char*256)()
    namesSize = 256
    status["getscalings"] = drDaq.UsbDrDaqGetScalings(chandle, channel, ctypes.byref(nScales), ctypes.byref(currentScale), ctypes.byref(names), namesSize)
    assert_pico_ok(status["getscalings"])

    # Set channel scaling 
    scalingNumber = 0 # pH scaling
    status["setscaling"] = drDaq.UsbDrDaqSetScalings(chandle, channel, scalingNumber)
    assert_pico_ok(status["setscaling"])

    # Set temperature compenstation
    enabled = 1
    status["phTemperatureCompensation"] = drDaq.UsbDrDaqPhTemperatureCompensation(chandle, enabled)
    assert_pico_ok(status["phTemperatureCompensation"])

    # Run block capture
    method = drDaq.USB_DRDAQ_BLOCK_METHOD["BM_SINGLE"]
    status["run"] = drDaq.UsbDrDaqRun(chandle, ideal_no_of_samples, method)
    assert_pico_ok(status["run"])

    ready = ctypes.c_int16(0)

    while ready.value == 0:
        status["ready"] = drDaq.UsbDrDaqReady(chandle, ctypes.byref(ready))

    # Retrieve data from device
    values = (ctypes.c_float * ideal_no_of_samples)()
    noOfValues = ctypes.c_uint32(ideal_no_of_samples)
    overflow = ctypes.c_uint16(0)
    triggerIndex = ctypes.c_uint32(0)
    status["getvaluesF"] = drDaq.UsbDrDaqGetValuesF(chandle, ctypes.byref(values), ctypes.byref(noOfValues), ctypes.byref(overflow), ctypes.byref(triggerIndex))
    assert_pico_ok(status["getvaluesF"])
    
    pH_value = np.mean(values)
    pH_std = np.std(values)
    print (pH_value, pH_std)
    


    # Disconnect the scope
    # handle = chandle
    status["close"] = drDaq.UsbDrDaqCloseUnit(chandle)
    assert_pico_ok(status["close"])

    # Display status returns
    print(status)
    return pH_value, pH_std


from centripeta import Dispenser
from centripeta.utils import Logger
from pycont.controller import MultiPumpController
from commanduino import CommandManager
import pandas as pd
import logging
import time

#Instantiate the command manager
mgr = CommandManager.from_configfile('platform_config_ports.json')
pumps = MultiPumpController.from_configfile('pycont_config.json')
a = Analyzer(mgr)
d = Dispenser(manager=mgr, pump_controller=pumps)


pH = []
pH_std = []
for i in range (8):
    a.vert_ph.home()
    a.horz_ph.home()
    # 4000 is the right step for cond_probe horizontal move to analyse
    a.horz_ph.move_to(4000)
    a.vert_ph.move_to(40000)
    print('pH analysing')
    time.sleep(30)

    # pH analysis, 5 second, sampling 1000 times
    H_value, pH_std_value = pH_test(5000000, 1000)
    pH = pH + [pH_value]
    pH_std = pH_std +[pH_std_value]

    a.vert_ph.home()

    # wait the sample droplet to drop
    time.sleep(10)

    # 34000 is the right step for cond_probe horizontal move to clean
    a.horz_ph.move_to(40000)
    a.vert_ph.move_to(40000)
    print('pH probe is cleaning')
    time.sleep(10)
    a.vert_ph.home()
    
    time.sleep (10)
    a.turn_wheel(n_turns = 1)




np.savetxt("pH_value.csv", pH, delimiter=",")