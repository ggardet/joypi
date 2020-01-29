#!/bin/bash

# Digits from left to right
# Hours
DIGIT_0=0x00
DIGIT_1=0x02
# Separator
COLON_DOTS=0x04
# Minutes
DIGIT_2=0x06
DIGIT_3=0x08

# Time to blink
TIME=10

# Display 0 (0x3F) on all digits
sudo i2cset -y 1 0x70 $DIGIT_0 0x3F
sudo i2cset -y 1 0x70 $DIGIT_1 0x3F
sudo i2cset -y 1 0x70 $DIGIT_2 0x3F
sudo i2cset -y 1 0x70 $DIGIT_3 0x3F

# Enable dots
sudo i2cset -y 1 0x70 $COLON_DOTS 0x02

# Enable display
sudo i2cset -y 1 0x70 0x81

# Blink at 1 Hz
sudo i2cset -y 1 0x70 0x85

sleep $TIME;

# Disable display
sudo i2cset -y 1 0x70 0x80

