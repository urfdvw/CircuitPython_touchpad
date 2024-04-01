# SPDX-FileCopyrightText: 2017 Tony DiCola for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test of the MPR121 capacitive touch sensor library.
# Will print out a message when any of the 12 capacitive touch inputs of the
# board are touched.  Open the serial REPL after running to see the output.
# Author: Tony DiCola
from time import monotonic, sleep
import board
import busio

# Import MPR121 module.
import adafruit_mpr121

# Create I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)

# Create MPR121 object.
mpr121 = adafruit_mpr121.MPR121(i2c)
N = 12
start_time = monotonic()
pad_max = [0] * N
pad_min = [100000] * N
while True:
    # run the test for 5s
    # in the mean time, slide on the ring for multiple cycles.
    for i in range(N):
        value = mpr121[i].raw_value
        if value == 0:
            continue
        pad_max[i] = max(pad_max[i], value)
        pad_min[i] = min(pad_min[i], value)
        # print(ring_max, ring_min)
        sleep(0.1)
    print("pad_max =", pad_max, ",")
    print("pad_min =", pad_min)
    
"""
pad_max = [284, 263, 272, 275, 271, 284, 278, 258, 257, 250, 246, 282] ,
pad_min = [128, 103, 108, 106, 106, 127, 109, 98, 88, 94, 88, 99]
"""