#!/bin/bash

# Read motion sensor value.
# 0 when nothing has been detected, 1 when something moved in front of the sensor

while true; do
	sudo gpioget gpiochip0 23
done

