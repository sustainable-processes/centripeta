#include <CommandHandler.h>
#include <CommandManager.h>
CommandManager cmdMgr;

/* Include the base files needed such as Accel Stepper, Servo etc */
#include <AccelStepper.h>
#include <LinearAccelStepperActuator.h>

/* Include the "Command" version of the above */
#include <CommandAccelStepper.h>
#include <CommandLinearAccelStepperActuator.h>

#include <CommandAnalogWrite.h>


/* Set up the base objects and Command objects */
AccelStepper stepperX(AccelStepper::DRIVER, 54, 55);
CommandLinearAccelStepperActuator X(stepperX, 3, 38);

AccelStepper stepperE1(AccelStepper::DRIVER, 36, 34);
CommandLinearAccelStepperActuator E1(stepperE1, 15, 30);

AccelStepper stepperZ(AccelStepper::DRIVER, 46, 48);
CommandLinearAccelStepperActuator Z(stepperZ, 18, 62);

CommandAnalogWrite fans(8);
CommandAnalogWrite dryingFans(9);


/* Do this for the rest of your devices */

void setup() {
    Serial.begin(115200); // Always 115200

    /* Register devices to the command manager */
    X.registerToCommandManager(cmdMgr, "hvisc"); 
    E1.registerToCommandManager(cmdMgr, "vvisc");
    Z.registerToCommandManager(cmdMgr, "vturb");
    fans.registerToCommandManager(cmdMgr, "a2fans");
    dryingFans.registerToCommandManager(cmdMgr, "dfans");

    
    /* Do this for the rest of your devices */
    cmdMgr.init();
}

void loop() {
    cmdMgr.update();
    /* Nothing else needed here */
}