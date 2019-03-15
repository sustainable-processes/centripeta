#include <CommandHandler.h>
#include <CommandManager.h>
CommandManager cmdMgr;

/* Include the base files needed such as Accel Stepper, Servo etc */
#include <AccelStepper.h>
#include <LinearAccelStepperActuator.h>

/* Include the "Command" version of the above */
#include <CommandAccelStepper.h>
#include <CommandLinearAccelStepperActuator.h>


/* Set up the base objects and Command objects */
AccelStepper stepperX(AccelStepper::DRIVER, 54, 55);
CommandLinearAccelStepperActuator X(stepperX, 3, 38);


/* Do this for the rest of your devices */

void setup() {
    Serial.begin(115200); // Always 115200

    /* Register devices to the command manager */
    X.registerToCommandManager(cmdMgr, "wd");
    
    /* Do this for the rest of your devices */
    cmdMgr.init();
}

void loop() {
    cmdMgr.update();
    /* Nothing else needed here */
}
