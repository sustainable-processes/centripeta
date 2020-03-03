# Centripeta

This is a set of tools for controlling the centripeta robots in publication 'Optimisation of formulations using robotic experiments driven by machine learning DoE'. 

![top-view](https://user-images.githubusercontent.com/18735742/75795699-9b33c800-5d6a-11ea-9955-d6d03a08946a.jpg)

This robot contains two parts: sample preparation part and sanple analysis part. A general scheme for the procedure is provided below. The continuous lines represent the materials flow, whereas dashed lines represent the information flow.

![image](https://user-images.githubusercontent.com/18735742/75796176-2d3bd080-5d6b-11ea-9f33-63945be6bdff.png = 250x)


## Installation

The easiest way to install centripeta is using pip:

```pip install -e git+https://github.com/sustainable-processes/centripeta@master#egg=centripeta```

<!-- I will pin the install to a particular release once we are ready to publish-->

### Prerequisites
 To use the code for pH measurement, PicoSDK C libraries will be need to install. For details please refer to Picotech website(https://www.picotech.com/downloads) and their [github repository](https://github.com/picotech/picosdk-python-wrappers)

<!-- This will depend on whether we keep the pH measurement part-->

## Running the experiments

The [protocol directory](https://github.com/sustainable-processes/centripeta/tree/master/protocols) contains the files for the robotic system control.





