# -*- coding: utf-8 -*-
from rt_dc_command import rt_dc_command
from rt_adb_command import rt_adb_command
from rtcommand import rtcommand
from rt_slack import rt_slack
import time, datetime, random
from PIL import Image

class rt_farm:
	@staticmethod
	def farm_exp():
		while (True):
			print("try to cast drive_skill")
			print(rt_dc_command.cast_drive_skill())
			print("sleep")
			time.sleep(5)
	
	def refresh_car_list(fake=False):
		#loop
		foundCar = False
		while (not foundCar):
			#make a adb tap event
			print('tap')
			x = 0x91 +  random.randint(0, 6) - 3 
			y = 0x29b + random.randint(0, 6) - 3
			print(rt_dc_command.tap(x, y))

			#waiting for refresh completed
			print("waiting for refresh completed")
			time.sleep(5)
			
			#screenshot
			print('taking a screenshot')
			timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y_%m_%d_%H_%M_%S')
			print(timestamp)
			file_name = timestamp + '.png'
			file_path = 'screenshots/' + file_name
			rt_adb_command.take_screenshot(file_path)

			#get a pixel of the image
			#file_path = 'screenshots/test.png'
			print('checking the screenshot')
			image = Image.open(file_path, 'r')
			pix = image.load()

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
			foundCar = ((r == 255 and g == 255 and b == 255) | (r == 31 and g == 35 and b == 23))
			print("existed:" + str(foundCar))
			time_interval = 30 + random.randint(10, 20)
			if not fake:
				time_interval = 10
			if (foundCar):
				#upload to slack if this is a car
				print('Car found, upload to slack')
				rt_slack.upload_car()
				
#				time_interval = 180
				
				#stroe picture to cars folder
				rtcommand.run_command('mv ' + file_path + ' cars/' + file_name)
			else:
				print('not found')
				
				if 5 == random.randint(1, 10):
					rtcommand.run_command('mv ' + file_path + ' nocars/' + file_name)
				
				if fake:
				#go to main screen
					rt_dc_command.go_to_home()
					time.sleep(time_interval)		
					#go back
					rt_dc_command.tap(400, 1698)			
					time.sleep(5)
				else:
					time.sleep(time_interval)