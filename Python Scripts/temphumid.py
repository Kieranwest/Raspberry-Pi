import RPi.GPIO as GPIO 
import Adafruit_DHT 
import I2C_LCD_driver 

mylcd = I2C_LCD_driver.lcd() 
sensor = Adafruit_DHT.DHT22 
pin = 16

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
GPIO.cleanup() 
  
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
temp = 'Temp:{0:0.1f}C'.format(temperature)
humid = 'Humidity:{1:0.1f}%'.format(temperature,humidity)
mylcd.lcd_display_string(temp, 1)
mylcd.lcd_display_string(humid, 2)
