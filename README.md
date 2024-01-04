# jetson_car

Self-driving car project.

![Alt text](misc/car.png)

## Requirements

This code runs on an Nvidia Jetson Nano with the JetPack SDK, developed and tested with Python 3.6.9.

It uses an L298N DC motor driver and 2 DC motors to drive. For steering it slows down one of the motors.

The CAD is designed with SolidWorks 2022 (all parts are SLDPRT). DXF and STL files are also provided for laser-cut and 3D-printed parts, respectively.

drive.py runs pwm.sh which runs sudo commands that set registers to configure GPIO pins 32 and 33 as PWM (needs a bunch of configuration for that to work, not needed if those pins are properly configured to PWM)

## Schematic

![schematic](misc/schematic.jpg)