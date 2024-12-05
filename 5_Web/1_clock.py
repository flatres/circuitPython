import os, ipaddress, wifi, ssl, socketpool, adafruit_requests
import time
import adafruit_ahtx0
import adafruit_rgbled
import board, busio, displayio, digitalio, terminalio
from i2cdisplaybus import I2CDisplayBus
from adafruit_display_text import label
import adafruit_displayio_ssd1306

# Setup
displayio.release_displays()
i2c = busio.I2C(board.GP17, board.GP16)  # uses board.SCL and board.SDA
display_bus = I2CDisplayBus(i2c, device_address=0x3c)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
display.root_group = displayio.Group()

led = digitalio.DigitalInOut(board.GP13)
led.direction = digitalio.Direction.OUTPUT

print("Connecting to WiFi")
wifi.radio.connect("Grid", "Wu@/=oPi3[/~S$")
print("Connected to WiFi")

#!!!!COPY AND PASTE THE ACCESS KEY HERE
key = ""
TIME_URL = f"https://io.adafruit.com/api/v2/flatres/integrations/time/strftime?x-aio-key={key}"
TIME_URL += "&fmt=%25H%3A%25M"

display.root_group = displayio.Group()
text = "Connected"
text_area = label.Label(terminalio.FONT, text=text, x=33, y=32)
display.root_group.append(text_area)
time.sleep(1)

pool = socketpool.SocketPool(wifi.radio)

#  prints IP address to REPL
print("My IP address is", wifi.radio.ipv4_address)

#  pings Google
try:
    ipv4 = ipaddress.ip_address("8.8.4.4")
    print("Ping google.com: %f ms" % (wifi.radio.ping(ipv4)*1000))
except Exception as e:
        print('Error')

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

light = False
oldTime = ""

alarmTime = '14:02'

while True:
    print("Fetching time from", TIME_URL)
    try:
        response = requests.get(TIME_URL)
        print(response.text)
        
        #Check the Alarm
        if response.text == alarmTime:
            led.value = True
        else:
            led.value = False
            
        #Write time to screen if it has changed    
        if response.text == oldTime:
            time.sleep(0.1)
        else:
            display.root_group = displayio.Group()
            text = response.text
            oldTime = text
            text_area = label.Label(terminalio.FONT, text=text, scale=3, x=20, y=22)
            display.root_group.append(text_area)
        response.close() 
        
    except Exception as e:
        print('Error')
    
    time.sleep(1)
   
#CHALLENGES

#1 Move the time so that it is displayed in the center of the screen
#2 Create a splash screen that is displayed until the wifi is connected
#3 Make the LED blink when the alarm goes off
#4 Make a buzzer sounds when the alarm goes off