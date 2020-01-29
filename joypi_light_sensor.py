#!/usr/bin/python3
# Based on example provided on JoyPi manual:
# https://joy-it.net/files/files/Produkte/RB-JoyPi/RB-JoyPi-Manual-02-09-2019.pdf

import smbus
import time

bus = smbus.SMBus(1)

class LightSensor():
	def __init__(self):
		# Define some constants from the datasheet
		self.DEVICE = 0x5c # Default device I2C address
		self.POWER_DOWN = 0x00 # No active state
		self.POWER_ON = 0x01 # Power on
		self.RESET = 0x07 # Reset data register value

		# Start measurement at 4lx resolution. Time typically 16ms.
		self.CONTINUOUS_LOW_RES_MODE = 0x13

		# Start measurement at 1lx resolution. Time typically 120ms
		self.CONTINUOUS_HIGH_RES_MODE_1 = 0x10

		# Start measurement at 0.5lx resolution. Time typically 120ms
		self.CONTINUOUS_HIGH_RES_MODE_2 = 0x11

		# Start measurement at 1lx resolution. Time typically 120ms
		# Device is automatically set to Power Down after measurement.
		self.ONE_TIME_HIGH_RES_MODE_1 = 0x20

		# Start measurement at 0.5lx resolution. Time typically 120ms
		# Device is automatically set to Power Down after measurement.
		self.ONE_TIME_HIGH_RES_MODE_2 = 0x21

		# Start measurement at 1lx resolution. Time typically 120ms
		# Device is automatically set to Power Down after measurement.
		self.ONE_TIME_LOW_RES_MODE = 0x23

	def convertToLx(self, data):
		# Convert 2 bytes of data into a decimal lux value
		return ((data[1] + (256 * data[0])) / 1.2)
 
	def readLight(self):
		data = bus.read_i2c_block_data(self.DEVICE,self.ONE_TIME_HIGH_RES_MODE_1)
		return self.convertToLx(data)

def main():
	sensor = LightSensor()
	try:
		while True:
			print("Light Level : " + str(sensor.readLight()) + " lx")
			time.sleep(0.5)
	except KeyboardInterrupt:
		pass

if __name__ == "__main__":
	main()

