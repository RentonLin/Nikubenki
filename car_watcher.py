# -*- coding: utf-8 -*-
import subprocess
from subprocess import call
import datetime
import time
from PIL import Image
import requests
import json

#loop
while (True):
	#make a adb tap event
	print('tap')
	x = 0x91
	y = 0x29b
	path_to_adb = '/Users/linweichao/Documents/platform-tools/adb '
	command = 'shell input tap ' + str(x) + ' ' + str(y)

	finnal_command = path_to_adb + command
	procId = subprocess.Popen(finnal_command, shell=True, stdin = subprocess.PIPE, stderr=subprocess.PIPE)
	stdout, stdrr = procId.communicate()
	print(stdout)
	print(stdrr)

	#waiting for refresh completed
	print("waiting for refresh completed")
	time.sleep(5)
	
	#screenshot
	print('taking a screenshot')
	timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y_%m_%d_%H_%M_%S')
	print(timestamp)
	file_path = 'screenshots/' + timestamp + '.png'
	command = 'exec-out screencap -p > ' + file_path
	finnal_command = path_to_adb + command
	procId = subprocess.Popen(finnal_command, shell=True, stdin = subprocess.PIPE, stderr=subprocess.PIPE)
	stdout, stdrr = procId.communicate()
	print(stdout)
	print(stdrr)

	#get a pixel of the image
	#file_path = 'screenshots/test.png'
	print('checking the screenshot')
	image = Image.open(file_path, 'r')
	pix = image.load()

	#point_x = 193
	#point_y = 813
	point_x = 74
	point_y = 775
	pixel = pix[point_x, point_y]
	print(pix[point_x, point_y])
	r = pixel[0]
	g = pixel[1]
	b = pixel[2]
	#color = hex(r * 16 * 16 * 16 * 16 + g * 16 * 16 + b)
	#print(r, g, b)
	#print(color)

	#todo now net error is not taken into consideration
	#check if any car exists
	car_exist = ((r == 255 and g == 255 and b == 255) | (r == 31 and g == 35 and b == 23))
	print("existed:" + str(car_exist))
	time_interval = 30
	if (car_exist):
		#upload to slack if this is a car
		print('Car found, upload to slack')
		#wait at least 2 minutes to refresh again
		headers = {'Content-Type': 'application/json'}
		params = {"icon_emoji": ":ghost:",
			"text": "出车啦~快来上啊(Ahe脸)",
			"username": "car_watcher_daze"}
		payload = json.dumps(params)
		print('payload is ' + payload)
		
		response = requests.post('https://hooks.slack.com/services/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', data=payload, headers=headers)
		print(response, response.status_code, response.text)
		
		time_interval = 180
	else:
		print('not found')
		
	#sleep according to whether this is a car
	time.sleep(time_interval)