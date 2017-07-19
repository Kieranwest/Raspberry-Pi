#Kieran's Custom LCD Display Script 24/06/2017
import RPi.GPIO as GPIO
import Adafruit_DHT
import I2C_LCD_driver
import socket
import time
import datetime

from urllib2 import urlopen

#Load I2C Driver
display = I2C_LCD_driver.lcd()

#Load DHT22 Driver
sensor = Adafruit_DHT.DHT22
sensor_pin = 16
GPIO.setmode(GPIO.BCM)

#Setting Pin 19 for Push Switch
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# First Menu #
menu = 0
display.lcd_display_string('Custom Display!', 1)
display.lcd_display_string('Press The Button', 2)

#Button Press Function
def buttonPressed(channel):
    global menu
    #If at Last Menu
    if menu == 4:
        #Reset Menu
        menu = 1
    else:
        #Next Menu
        menu += 1
    #First Menu - Temperature
    if menu == 1:
        display.lcd_clear()
    #Second Menu - Public IP
    elif menu == 2:
        display.lcd_clear()
        display.lcd_display_string("Public IP", 1)
        display.lcd_display_string(getPublicIP(), 2)
    #Third Menu - Local IP
    elif menu == 3:
        display.lcd_clear()
        display.lcd_display_string("Local IP", 1)
        display.lcd_display_string(getPrivateIP(), 2)
    elif menu == 4:
        display.lcd_clear()

def getPublicIP():
    #Reading RAW Data from HTML Page
    ip = urlopen('http://ip.42.pl/raw').read()
    #Returning Read Data
    return ip

def getPrivateIP():
    #Assigning Socket Variable
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #Opening a Socket
    s.connect(("8.8.8.8", 80))
    #Returning Original Route
    return s.getsockname()[0]

#Button Listener
GPIO.add_event_detect(19, GPIO.FALLING, callback=buttonPressed, bouncetime=1000)
try:
    #10 Second Loop
    while True:
        if menu == 0:
            menu = 4

        if menu == 4:
            d = time.strftime('%A %d %B')
            t = time.strftime('%H:%M:%S')
            display.lcd_clear()
            display.lcd_display_string(d, 1)
            display.lcd_display_string(t, 2)
            time.sleep(1)

        if menu == 1:
            humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_pin)
            temp = 'Temp:{0:0.1f}'.format(temperature)
            humid = 'Humidity:{1:0.1f}%'.format(temperature,humidity)
            display.lcd_clear()
            display.lcd_display_string(temp + chr(223) + 'C', 1)
            display.lcd_display_string(humid, 2)
            time.sleep(10)
except KeyboardInterrupt:
    GPIO.cleanup()
    display.lcd_clear()
    print "\n"
    print "Exited Cleanly"
