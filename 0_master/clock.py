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

#splash screen
text = "Hey Jemima!"
text_area = label.Label(terminalio.FONT, text=text, x=33, y=32)
display.root_group.append(text_area)
time.sleep(2)

display.root_group = displayio.Group()
text = "Connecting..."
text_area = label.Label(terminalio.FONT, text=text, x=33, y=32)
display.root_group.append(text_area)

RED = board.GP2
GREEN = board.GP1
BLUE = board.GP0

# Create the RGB LED object
led = adafruit_rgbled.RGBLED(RED, GREEN, BLUE)

switch1 = digitalio.DigitalInOut(board.GP4)
switch1.direction = digitalio.Direction.INPUT
switch1.pull = digitalio.Pull.UP

print("Connecting to WiFi")

key = ""
TIME_URL = f"https://io.adafruit.com/api/v2/flatres/integrations/time/strftime?x-aio-key={key}"
TIME_URL += "&fmt=%25H%3A%25M"

#  connect to your SSID
wifi.radio.connect("3MobileWiFi-2G", "A1b2C3d4E5")

print("Connected to WiFi")

display.root_group = displayio.Group()
text = "Connected"
text_area = label.Label(terminalio.FONT, text=text, x=33, y=32)
display.root_group.append(text_area)
time.sleep(1)

pool = socketpool.SocketPool(wifi.radio)

#  prints MAC address to REPL
print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])

#  prints IP address to REPL
print("My IP address is", wifi.radio.ipv4_address)

#  pings Google
ipv4 = ipaddress.ip_address("8.8.4.4")
print("Ping google.com: %f ms" % (wifi.radio.ping(ipv4)*1000))

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

light = False
oldTime = ""

sensor = adafruit_ahtx0.AHTx0(i2c)

while True:
    if switch1.value == False:
      light = not light
      #time.sleep(0.2)
    if light:
        led.color = (255, 00, 0)
    else:
        led.color = (0, 0, 0)
    print("Fetching text from", TIME_URL)
    response = requests.get(TIME_URL)
    print(response.text)
    if response.text == oldTime:
        time.sleep(0.1)
    else:
        display.root_group = displayio.Group()
        text = response.text
        oldTime = text
        temperature = sensor.temperature
        humidity = sensor.relative_humidity
        print("\nTemperature: %0.1f C" % temperature)
        print("Humidity: %0.1f %%" % humidity)
        text_area = label.Label(terminalio.FONT, text=text, scale=3, x=20, y=22)
        display.root_group.append(text_area)
        
        #update data
        text = "T: %0.1f" % temperature
        text_area = label.Label(terminalio.FONT, text=text, x=5, y=55)
        display.root_group.append(text_area)
        
        text = "H: %0.1f" % humidity
        text_area = label.Label(terminalio.FONT, text=text, x=80, y=55)
        display.root_group.append(text_area)
    
    time.sleep(1)

