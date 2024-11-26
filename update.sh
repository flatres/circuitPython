#!/bin/bash
git stash
git pull origin main

sudo  mkdir /media/usb
sudo mount /dev/sda1 /media/usb

cd 0_master
cd libs
cd adafruit
cd lib
cp adafruit_rgbled.mpy /media/usb/lib/

#oled
cp adafruit_ssd1306.mpy /media/usb/lib/
cp adafruit_displayio_ssd1306.mpy /media/usb/lib/
cp adafruit_framebuf.mpy /media/usb/lib/
cp -r adafruit_display_text /media/usb/lib/

#env sensor AHT20
cp -r adafruit_bus_device /media/usb/lib/
cp adafruit_ahtx0.mpy /media/usb/lib/

#motor
cp -r adafruit_motor /media/usb/lib/

