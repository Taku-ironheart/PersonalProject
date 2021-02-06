#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import grovepi
import math

#url = "https://notify-api.line.me/api/notify" 
#token = "KSrZELTc6hzCPOhyhRGj2eEvR4GgnswejJLDYhY0ieP"
#headers = {"Authorization" : "Bearer "+ token} 
#message =  "ラズパイからメッセージを受信しました！" 
#payload = {"message" :  message} 
#r = requests.post(url, headers = headers, params=payload)


# Connect the Grove Temperature & Humidity Sensor Pro to digital port D4
# This example uses the blue colored sensor.
# SIG,NC,VCC,GND
sensor = 4  # The Sensor goes on digital port 4.

# temp_humidity_sensor_type
# Grove Base Kit comes with the blue sensor.
blue = 0    # The Blue colored sensor.
white = 1   # The White colored sensor.

j=1
for i in range(10):
	[temp,humidity] = grovepi.dht(sensor,blue)
	if math.isnan(temp) == False and math.isnan(humidity) == False:
                print(j)
                print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))
                total_j = j + 1
                total_temp +=temp
                total_humidity +=humidity
        else:
                continue
    

avrg_temp=temp / j
avrg_humidity=humidity / j

print("avrg_temp:"+ str(avrg_temp))
print("avrg_humidity:" + str(avrg_humidity))

