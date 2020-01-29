#!/usr/bin/python3

import spidev
import time

spi = spidev.SpiDev()
bus = 0
device = 1
spi.open(bus, device)

# Settings (for example)
spi.max_speed_hz = 10000000 # 10 MHz
#spi.mode = 0b01

to_send = [0x0F, 0x01]
spi.xfer(to_send)
time.sleep(1)
to_send = [0x0F, 0x00]
spi.xfer(to_send)

# Normal operation
to_send = [0x0C, 0x01]
spi.xfer(to_send)

# No decoding
to_send = [0x09, 0x00]
spi.xfer(to_send)

# Intensity: max 0x0F
to_send = [0x0A, 0x0F]
spi.xfer(to_send)

# Make use of all leds
to_send = [0x0B, 0x07]
spi.xfer(to_send)

# Switch OFF all leds
rows = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08]
for row in rows:
    to_send = [row, 0x00]
    spi.xfer(to_send)

# Light on, 1 line after an other
try:
    while True:
        for row in rows:
            to_send = [row, 0xFF]
            spi.xfer(to_send)
            time.sleep(1)
            to_send = [row, 0x00]
            spi.xfer(to_send)
except KeyboardInterrupt:
    # Switch all leds on exit
    for row in rows:
        to_send = [row, 0x00]
        spi.xfer(to_send)
    # Release SPI
    spi.close

