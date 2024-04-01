#%% import and define
import time
from time import sleep
import board
import busio
import adafruit_mpr121
from touchpad import TouchBarPhysics
import usb_hid
from adafruit_hid.mouse import Mouse
i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)
mouse = Mouse(usb_hid.devices)
#%%
bar_phy_y = TouchBarPhysics(
    pads=[mpr121[i] for i in range(5, -1, -1)],
    pad_max=[272, 256, 264, 267, 263, 277],
    pad_min=[133, 130, 147, 140, 135, 139],
    touch_high=False,
)

bar_phy_x = TouchBarPhysics(
    pads=[mpr121[i] for i in range(6, 12)],
    pad_max=[272, 256, 264, 267, 263, 277],
    pad_min=[133, 130, 147, 140, 135, 139],
    touch_high=False,
)

print('startplot:', 'x', 'z')
for i in range(100000):
    sleep(0.01)
    raw_x = bar_phy_x.get()
    raw_y = bar_phy_y.get()
    if raw_x.z > 0.5 and raw_y.z > 0.5:
        print(raw_x.x, raw_y.x)