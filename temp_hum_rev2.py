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

num=0
total_temp=0
total_humidity=0
for i in range(50):
        [temp,humidity] = grovepi.dht(sensor,blue)
        if math.isnan(temp) == False and math.isnan(humidity) == False:
                num=num+1
                print(num)
                print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))
                total_temp +=temp
                total_humidity +=humidity
        else:
                #print("########")
                continue

avrg_temp=total_temp / num
avrg_humidity=total_humidity / num

print("avrg_temp:"+ str(avrg_temp))
print("avrg_humidity:" + str(avrg_humidity))

#url = "https://notify-api.line.me/api/notify" 
#token = "KSrZELTc6hzCPOhyhRGj2eEvR4GgnswejJLDYhY0ieP"
#headers = {"Authorization" : "Bearer "+ token} 
#message =  "ラズパイからメッセージを受信しました！" 
#payload = {"message" :  message} 
#r = requests.post(url, headers = headers, params=payload)

url = "https://notify-api.line.me/api/notify" 
token = "KSrZELTc6hzCPOhyhRGj2eEvR4GgnswejJLDYhY0ieP"
headers = {"Authorization" : "Bearer "+ token} 
message = ["気温" + str(format(avrg_temp,'.1f')) + "C", "湿度" + str(format(avrg_humidity,'.1f')) + "％"]
payload = {"message" :  message} 
r = requests.post(url, headers = headers, params=payload)
