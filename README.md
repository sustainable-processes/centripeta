# Centripeta

This is a set of tools for controlling the centripeta robots in the publication "[Optimisation of formulations using robotic experiments driven by machine learning DoE](https://www.cell.com/cell-reports-physical-science/fulltext/S2666-3864(20)30321-0)."

![top-view](https://user-images.githubusercontent.com/18735742/75795699-9b33c800-5d6a-11ea-9955-d6d03a08946a.jpg)

This robot contains two parts: sample preparation part and sanple analysis part. A general scheme for the procedure is provided below. The continuous lines represent the materials flow, whereas dashed lines represent the information flow.

![image](https://user-images.githubusercontent.com/18735742/75796176-2d3bd080-5d6b-11ea-9f33-63945be6bdff.png)


## Installation

The easiest way to install centripeta is using pip:

```pip install -e git+https://github.com/sustainable-processes/centripeta@master#egg=centripeta```

<!-- I will pin the install to a particular release once we are ready to publish-->

 To use the code for pH measurement, the PicoSDK C libraries need to installed. For details, please refer to Picotech website(https://www.picotech.com/downloads) and their [github repository](https://github.com/picotech/picosdk-python-wrappers).

<!-- This will depend on whether we keep the pH measurement part-->

## Running the experiments

Below is a simple example for running the experiments.

```python
from centripeta import Dispenser
from pycont.controller import MultiPumpController
from commanduino import CommandManager
import pandas as pd

#This is the CSV file with the conditions to dispense into the vials
CONDITIONS_FILE="xp_initial_0.csv"

#Instantiate the communication with the robot
mgr = CommandManager.from_configfile('platform_config_ports.json')
pumps = MultiPumpController.from_configfile('pycont_config_less.json')
d = Dispenser(manager=mgr, pump_controller=pumps)

# Read in conditions and run the robot
conditions = pd.read_csv(CONDITION_FILE)
for i, condition in conditions.iterrows():
    #Dispense each surfactant
    d.dispense(pump_name="Plantacare818", volume=condition['Plantacare818'], speed_in=1500)
    d.dispense(pump_name="Texapon", volume =condition['Texapon'], speed_in=1500) 
    d.dispense(pump_name="DehytonAB30", volume=condition['DehytonAB30'], speed_in=1500)
    d.dispense(pump_name="ArlyponTT", volume=condition['ArlyponTT'])
    d.dispense(pump_name="CC7BZ", volume=condition['CC7BZ'])

    #Wait and dispense water
    time.sleep(10)
    d.dispense(pump_name="water", volume=condition['water'])

    #Wait and turn the wheel
    time.sleep(5)
    d.turn_wheel(n_turns=1)
    print('finish sample' + 'i')
print('Done!!')
```
To see more examples, take a look at the [protocol directory](https://github.com/sustainable-processes/centripeta/tree/master/protocols), which contains the files for the robotic system control.
