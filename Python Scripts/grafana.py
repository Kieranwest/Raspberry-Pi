import time
import sys
import datetime
from influxdb import InfluxDBClient
import Adafruit_DHT
import json

# Set this variables, influxDB should be localhost on Pi
host = "localhost"
port = 8086
user = "root"
password = "root"

# The database we created
dbname = "monitoring"

# Create the InfluxDB object
client = InfluxDBClient(host, port, user, password, dbname)

iso = time.ctime()
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 16)
if humidity is not None:
        humidity_1 = humidity
if temperature is not None:
        temperature_1 = temperature
json_body = [
{
    "measurement": "monitoring",
    "tags": {"location": "homelab"},
    "fields": {
	"temp": format(temperature_1, '.2f'),
	"humidity": format(humidity_1, '.2f')
}
}]

# Write JSON to InfluxDB
if temperature > 50:
    quit()
if humidity > 100:
    quit()

client.write_points(json_body)
