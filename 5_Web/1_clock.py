import os, ipaddress, wifi, ssl, socketpool, adafruit_requests
import time
import adafruit_ahtx0
import adafruit_rgbled
import board, busio, displayio, digitalio, terminalio
from i2cdisplaybus import I2CDisplayBus
from adafruit_display_text import label
import adafruit_displayio_ssd1306

# Setup
print("Connecting to WiFi")
wifi.radio.connect("MC-WIFI", "Wu@/=oPi3[/~S$")
print("Connected to WiFi")

#!!!!COPY AND PASTE THE ACCESS KEY HERE
k = "aio_"
k = 'x-aio-key=' + k + "GeLK691wqaYsOf1CDcbAjhH8FUqk"
TIME_URL = f"https://io.adafruit.com/api/v2/flatres/integrations/time/strftime?{k}"
TIME_URL += "&fmt=%25H%3A%25M"

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
        response.close() 
        
    except Exception as e:
        print('Error')
    
    time.sleep(1)
   
#CHALLENGES

#1 Move the time so that it is displayed in the center of the screen
#2 Create a splash screen that is displayed until the wifi is connected
#3 Make the LED blink when the alarm goes off
#4 Make a buzzer sounds when the alarm goes off