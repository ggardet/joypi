#!/bin/bash

# AMount of time to switch the relay ON
time_on=10

sudo gpioset -m time -s $time_on -l  gpiochip0 21=1

