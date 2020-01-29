#!/bin/bash

# The tilt sensor is on pin15 (gpio22), but you need to switch ON switch number 2, on right DIP switch, the others to OFF. 
# Read the value returned by the sensor (0 when tilt to right, 1 when tilt to left):

while true; do
	sudo gpioget gpiochip0 22
done

