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
cp adafruit_ssd1306.mpy /media/usb/lib/
cp -r adafruit_display_text /media/usb/lib/
