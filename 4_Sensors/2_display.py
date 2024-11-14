# import libraries
import board, busio, displayio, digitalio, time, terminalio

from i2cdisplaybus import I2CDisplayBus
from adafruit_display_text import label
import adafruit_displayio_ssd1306

import adafruit_ahtx0

#Setup
i2c = busio.I2C(board.GP17, board.GP16)  # uses board.SCL and board.SDA

displayio.release_displays()
display_bus = I2CDisplayBus(i2c, device_address=0x3c)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
display.root_group = displayio.Group()

sensor = adafruit_ahtx0.AHTx0(i2c)

while True:
    temperature = sensor.temperature
    humidity = sensor.relative_humidity
    
    print("\nTemperature: %0.1f C" % temperature)
    print("Humidity: %0.1f %%" % humidity)
    
    #clear the display     
    display.root_group = displayio.Group()
    
    #update data
    text = "Temp: %0.1f C" % temperature
    text_area = label.Label(terminalio.FONT, text=text, x=5, y=25)
    display.root_group.append(text_area)
    
    text = "Humidity: %0.1f %%" % humidity
    text_area = label.Label(terminalio.FONT, text=text, x=5, y=42)
    display.root_group.append(text_area)
    
    time.sleep(2)